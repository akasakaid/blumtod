import os
import sys
import time
import json
import random
import requests
from json import dumps as dp, loads as ld
from datetime import datetime
from colorama import *
from urllib.parse import unquote

init(autoreset=True)

merah = Fore.LIGHTRED_EX
putih = Fore.LIGHTWHITE_EX
hijau = Fore.LIGHTGREEN_EX
kuning = Fore.LIGHTYELLOW_EX
biru = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL
hitam = Fore.LIGHTBLACK_EX


class BlumTod:
    def __init__(self):
        self.base_headers = {
            "accept": "application/json, text/plain, */*",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
            "content-type": "application/json",
            "origin": "https://telegram.blum.codes",
            "x-requested-with": "org.telegram.messenger",
            "sec-fetch-site": "same-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": "https://telegram.blum.codes/",
            "accept-encoding": "gzip, deflate",
            "accept-language": "en,en-US;q=0.9",
        }
        self.garis = putih + "~" * 50

    def renew_access_token(self, tg_data):
        headers = self.base_headers.copy()
        data = dp(
            {
                "query": tg_data,
            },
        )
        headers["Content-Length"] = str(len(data))
        url = "https://gateway.blum.codes/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"
        res = self.http(url, headers, data)
        if "token" not in res.json().keys():
            self.log(f"{merah}'token' is not found in response, check you data !!")
            return

        access_token = res.json()["token"]["access"]
        self.log(f"{hijau}success get access token ")
        return access_token

    def solve_task(self, access_token):
        url_task = "https://game-domain.blum.codes/api/v1/tasks"
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {access_token}"
        res = self.http(url_task, headers)
        for task in res.json():
            task_id = task["id"]
            task_title = task["title"]
            task_status = task["status"]
            if task_status == "NOT_STARTED":
                url_start = (
                    f"https://game-domain.blum.codes/api/v1/tasks/{task_id}/start"
                )
                res = self.http(url_start, headers, "")
                if "message" in res.text:
                    continue

                url_claim = (
                    f"https://game-domain.blum.codes/api/v1/tasks/{task_id}/claim"
                )
                res = self.http(url_claim, headers, "")
                if "message" in res.text:
                    continue

                status = res.json()["status"]
                if status == "CLAIMED":
                    self.log(f"{hijau}success complete task {task_title} !")
                    continue

            self.log(f"{kuning}already complete task {task_title} !")

    def claim_farming(self, access_token):
        url = "https://game-domain.blum.codes/api/v1/farming/claim"
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {access_token}"
        res = self.http(url, headers, "")
        balance = res.json()["availableBalance"]
        self.log(f"{hijau}balance after claim : {balance}")
        return

    def get_balance(self, access_token,only_show_balance=False):
        url = "https://game-domain.blum.codes/api/v1/user/balance"
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {access_token}"
        res = self.http(url, headers)
        balance = res.json()["availableBalance"]
        self.log(f"{hijau}balance : {putih}{balance}")
        if only_show_balance:
            return
        timestamp = round(res.json()["timestamp"] / 1000)
        if "farming" not in res.json().keys():
            return False, "not_started"
        end_farming = round(res.json()["farming"]["endTime"] / 1000)
        if timestamp > end_farming:
            self.log(f"{hijau}now is time to claim farming !")
            return True, end_farming

        self.log(f"{kuning}not time to claim farming !")
        end_date = datetime.fromtimestamp(end_farming)
        self.log(f'{hijau}end farming : {putih}{end_date}')
        return False, end_farming

    def start_farming(self, access_token):
        url = "https://game-domain.blum.codes/api/v1/farming/start"
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {access_token}"
        res = self.http(url, headers, "")
        end = res.json()["endTime"]
        end_date = datetime.fromtimestamp(end / 1000)
        self.log(f"{hijau}start farming successfully !")
        self.log(f"{hijau}end farming : {putih}{end_date}")
        return round(end / 1000)

    def get_friend(self, access_token):
        url = "https://gateway.blum.codes/v1/friends/balance"
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {access_token}"
        res = self.http(url, headers)
        can_claim = res.json()["canClaim"]
        limit_invite = res.json()["limitInvitation"]
        amount_claim = res.json()["amountForClaim"]
        ref_code = res.json()["referralToken"]
        self.log(f"{putih}limit invitation : {hijau}{limit_invite}")
        self.log(f"{hijau}claim amount : {putih}{amount_claim}")
        self.log(f"{putih}can claim : {hijau}{can_claim}")
        if can_claim:
            url_claim = "https://gateway.blum.codes/v1/friends/claim"
            res = self.http(url_claim, headers, "")
            if "claimBalance" in res.json().keys():
                self.log(f"{hijau}success claim referral bonus !")
                return
            self.log(f"{merah}failed claim referral bonus !")
            return
    
    def playgame(self,access_token):
        url_play = "https://game-domain.blum.codes/api/v1/game/play"
        url_claim = "https://game-domain.blum.codes/api/v1/game/claim"
        url_balance = "https://game-domain.blum.codes/api/v1/user/balance"
        config = json.loads(open('config.json','r').read())
        game_cfg = config['game_point']
        low = game_cfg['low']
        high = game_cfg['high']
        if low > high:
            self.log(f'{kuning}high value must be higher than lower value')
            return
        headers = self.base_headers.copy()
        headers['Authorization'] = f"Bearer {access_token}"
        res = self.http(url_balance,headers)
        play = res.json()['playPasses']
        self.log(f'{hijau}you have {putih}{play}{hijau} game ticket')
        for i in range(play):
            res = self.http(url_play,headers,'')
            game_id = res.json()['gameId']
            self.countdown(30)
            point = random.randint(low,high)
            data = json.dumps({"gameId":game_id,"points":point})
            res = self.http(url_claim,headers,data)
            if "OK" in res.text:
                self.log(f'{hijau}success earn {putih}{point}{hijau} from game !')
                self.get_balance(access_token,only_show_balance=True)
                continue
            
            self.log(f'{merah}failed earn {putih}{point}{merah} from game !')
            continue

    def data_parsing(self, data):
        redata = {}
        for i in unquote(data).split("&"):
            key, value = i.split("=")
            redata[key] = value

        return redata

    def log(self, message):
        now = datetime.now().isoformat(" ").split(".")[0]
        print(f"{hitam}[{now}]{reset} {message}")

    def http(self, url, headers, data=None):
        while True:
            try:
                if data is None:
                    headers["content-length"] = "0"
                    res = requests.get(url, headers=headers, timeout=30)
                    open(".http_request.log", "a", encoding="utf-8").write(
                        res.text + "\n"
                    )
                    if "<html>" in res.text:
                        time.sleep(2)
                        continue
                    
                    return res

                if data == "":
                    res = requests.post(url, headers=headers, timeout=30)
                    open(".http_request.log", "a", encoding="utf-8").write(
                        res.text + "\n"
                    )
                    if "<html>" in res.text:
                        time.sleep(2)
                        continue
                    
                    return res

                res = requests.post(url, headers=headers, data=data, timeout=30)
                open(".http_request.log", "a", encoding="utf-8").write(res.text + "\n")
                if "<html>" in res.text:
                    time.sleep(2)
                    continue
                
                return res

            except (
                requests.exceptions.ConnectionError,
                requests.exceptions.ConnectTimeout,
                requests.exceptions.ReadTimeout,
            ):
                self.log(f"{merah}connection error")

    def countdown(self, t):
        while t:
            menit, detik = divmod(t, 60)
            jam, menit = divmod(menit, 60)
            jam = str(jam).zfill(2)
            menit = str(menit).zfill(2)
            detik = str(detik).zfill(2)
            print(f"{putih}waiting until {jam}:{menit}:{detik} ", flush=True, end="\r")
            t -= 1
            time.sleep(1)
        print("                          ", flush=True, end="\r")

    def main(self):
        banner = f"""
    {hijau}AUTO CLAIM FOR {putih}BLUM {hijau}/ {biru}@BlumCryptoBot
    
    {hijau}By : {putih}t.me/AkasakaID
    {putih}Github : {hijau}@AkasakaID
    
    {hijau}Message : {putih}Dont forget to 'git pull' maybe i update the bot !
        """
        arg = sys.argv
        if "noclear" not in arg:
            os.system("cls" if os.name == "nt" else "clear")
        print(banner)
        datas = open("data.txt", "r").read().splitlines()
        self.log(f"{hijau}total account : {putih}{len(datas)}")
        if len(datas) <= 0:
            self.log(f"{merah}add data account in data.txt")
            sys.exit()

        self.log(self.garis)
        while True:
            list_countdown = []
            for no,data in enumerate(datas):
                self.log(f"{hijau}account number - {putih}{no + 1}")
                data_parse = self.data_parsing(data)
                user = json.loads(data_parse['user'])
                self.log(f"{hijau}login as : {putih}{user['first_name']}")
                access_token = self.renew_access_token(data)
                self.get_friend(access_token)
                self.solve_task(access_token)
                status, res_bal = self.get_balance(access_token)
                if status:
                    self.claim_farming(access_token)
                    res_bal = self.start_farming(access_token)
                if isinstance(res_bal, str):
                    res_bal = self.start_farming(access_token)
                list_countdown.append(res_bal)
                self.playgame(access_token)
                self.log(self.garis)
            min_countdown = min(list_countdown)
            now = int(time.time())
            result = min_countdown - now
            if result <= 0:
                continue

            self.countdown(result)


if __name__ == "__main__":
    try:
        app = BlumTod()
        app.main()
    except KeyboardInterrupt:
        sys.exit()
