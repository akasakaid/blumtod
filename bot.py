import os
import sys
import time
import json
import random
import requests
import argparse
from json import dumps as dp, loads as ld
from datetime import datetime
from colorama import *
from urllib.parse import unquote, parse_qs
from base64 import b64decode

init(autoreset=True)

merah = Fore.LIGHTRED_EX
putih = Fore.LIGHTWHITE_EX
hijau = Fore.LIGHTGREEN_EX
kuning = Fore.LIGHTYELLOW_EX
biru = Fore.LIGHTBLUE_EX
reset = Style.RESET_ALL
hitam = Fore.LIGHTBLACK_EX
magenta = Fore.LIGHTMAGENTA_EX


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
        url = "https://user-domain.blum.codes/api/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"
        res = self.http(url, headers, data)
        token = res.json().get("token")
        if token is None:
            self.log(f"{merah}'token' is not found in response, check you data !!")
            return 0

        access_token = token.get("access")
        self.log(f"{hijau}success get access token ")
        return access_token

    def solve_task(self, access_token):
        url_task = "https://game-domain.blum.codes/api/v1/tasks"
        ignore_tasks = [
            "39391eb2-f031-4954-bd8a-e7aecbb1f192",  # wallet connect
            "d3716390-ce5b-4c26-b82e-e45ea7eba258",  # invite task
            "f382ec3f-089d-46de-b921-b92adfd3327a", # invite task
            "220ee7b1-cca4-4af8-838a-2001cb42b813", # invite task
            "5ecf9c15-d477-420b-badf-058537489524", # invite task
            "c4e04f2e-bbf5-4e31-917b-8bfa7c4aa3aa" # invite task
        ]
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {access_token}"
        res = self.http(url_task, headers)
        for tasks in res.json():
            if isinstance(tasks, str):
                self.log(f"{kuning}failed get task list !")
                return
            for k in list(tasks.keys()):
                for t in tasks.get(k):
                    for task in t.get("tasks"):
                        task_id = task.get("id")
                        task_title = task.get("title")
                        task_status = task.get("status")
                        start_task_url = f"https://game-domain.blum.codes/api/v1/tasks/{task_id}/start"
                        claim_task_url = f"https://game-domain.blum.codes/api/v1/tasks/{task_id}/claim"
                        if task_id in ignore_tasks:
                            continue
                        if task_status == "FINISHED":
                            self.log(
                                f"{kuning}already complete task id {putih}{task_id} !"
                            )
                            continue
                        if task_status == "READY_FOR_CLAIM":
                            _res = self.http(claim_task_url, headers, "")
                            _status = _res.json().get("status")
                            if _status == "FINISHED":
                                self.log(
                                    f"{hijau}success complete task id {putih}{task_id} !"
                                )
                                continue

                        _res = self.http(start_task_url, headers, "")
                        self.countdown(5)
                        _status = _res.json().get("status")
                        if _status == "STARTED":
                            _res = self.http(claim_task_url, headers, "")
                            _status = _res.json().get("status")
                            if _status == "FINISHED":
                                self.log(
                                    f"{hijau}success complete task id {putih}{task_id} !"
                                )
                                continue

    def set_proxy(self, proxy=None):
        self.ses = requests.Session()
        if proxy is not None:
            self.ses.proxies.update({"http": proxy, "https": proxy})

    def claim_farming(self, access_token):
        url = "https://game-domain.blum.codes/api/v1/farming/claim"
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {access_token}"
        res = self.http(url, headers, "")
        balance = res.json().get("availableBalance", 0)
        self.log(f"{hijau}balance after claim : {putih}{balance}")
        return

    def get_balance(self, access_token, only_show_balance=False):
        url = "https://game-domain.blum.codes/api/v1/user/balance"
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {access_token}"
        while True:
            res = self.http(url, headers)
            balance = res.json().get("availableBalance", 0)
            self.log(f"{hijau}balance : {putih}{balance}")
            if only_show_balance:
                return
            timestamp = res.json().get("timestamp")
            if timestamp is None:
                self.countdown(3)
                continue
            timestamp = round(timestamp / 1000)
            if "farming" not in res.json().keys():
                return False, "not_started"
            end_farming = res.json().get("farming", {}).get("endTime")
            if end_farming is None:
                self.countdown(3)
                continue
            break
        end_farming = round(end_farming / 1000)
        if timestamp > end_farming:
            self.log(f"{hijau}now is time to claim farming !")
            return True, end_farming

        self.log(f"{kuning}not time to claim farming !")
        end_date = datetime.fromtimestamp(end_farming)
        self.log(f"{hijau}end farming : {putih}{end_date}")
        return False, end_farming

    def start_farming(self, access_token):
        url = "https://game-domain.blum.codes/api/v1/farming/start"
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {access_token}"
        while True:
            res = self.http(url, headers, "")
            end = res.json().get("endTime")
            if end is None:
                self.countdown(3)
                continue
            break

        end_date = datetime.fromtimestamp(end / 1000)
        self.log(f"{hijau}start farming successfully !")
        self.log(f"{hijau}end farming : {putih}{end_date}")
        return round(end / 1000)

    def get_friend(self, access_token):
        url = "https://user-domain.blum.codes/api/v1/friends/balance"
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {access_token}"
        res = self.http(url, headers)
        can_claim = res.json().get("canClaim", False)
        limit_invite = res.json().get("limitInvitation", 0)
        amount_claim = res.json().get("amountForClaim")
        self.log(f"{putih}limit invitation : {hijau}{limit_invite}")
        self.log(f"{hijau}referral balance : {putih}{amount_claim}")
        self.log(f"{putih}can claim referral : {hijau}{can_claim}")
        if can_claim:
            url_claim = "https://user-domain.blum.codes/api/v1/friends/claim"
            res = self.http(url_claim, headers, "")
            if res.json().get("claimBalance") is not None:
                self.log(f"{hijau}success claim referral bonus !")
                return
            self.log(f"{merah}failed claim referral bonus !")
            return

    def checkin(self, access_token):
        url = "https://game-domain.blum.codes/api/v1/daily-reward?offset=-420"
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {access_token}"
        res = self.http(url, headers)
        if res.status_code == 404:
            self.log(f"{kuning}already check in today !")
            return
        res = self.http(url, headers, "")
        if "ok" in res.text.lower():
            self.log(f"{hijau}success check in today !")
            return

        self.log(f"{merah}failed check in today !")
        return

    def playgame(self, access_token):
        url_play = "https://game-domain.blum.codes/api/v1/game/play"
        url_claim = "https://game-domain.blum.codes/api/v1/game/claim"
        url_balance = "https://game-domain.blum.codes/api/v1/user/balance"
        headers = self.base_headers.copy()
        headers["Authorization"] = f"Bearer {access_token}"
        while True:
            res = self.http(url_balance, headers)
            play = res.json().get("playPasses")
            if play is None:
                self.log(f"{kuning}failed get game ticket !")
                break
            self.log(f"{hijau}you have {putih}{play}{hijau} game ticket")
            if play <= 0:
                return
            for i in range(play):
                if self.is_expired(access_token):
                    return True
                res = self.http(url_play, headers, "")
                game_id = res.json().get("gameId")
                if game_id is None:
                    message = res.json().get("message", "")
                    if message == "cannot start game":
                        self.log(
                            f"{kuning}{message},will be tried again in the next round."
                        )
                        return False
                    self.log(f"{kuning}{message}")
                    continue
                while True:
                    self.countdown(30)
                    point = random.randint(self.MIN_WIN, self.MAX_WIN)
                    data = json.dumps({"gameId": game_id, "points": point})
                    res = self.http(url_claim, headers, data)
                    if "OK" in res.text:
                        self.log(
                            f"{hijau}success earn {putih}{point}{hijau} from game !"
                        )
                        self.get_balance(access_token, only_show_balance=True)
                        break

                    message = res.json().get("message", "")
                    if message == "game session not finished":
                        continue

                    self.log(f"{merah}failed earn {putih}{point}{merah} from game !")
                    break

    def data_parsing(self, data):
        return {k: v[0] for k, v in parse_qs(data).items()}

    def log(self, message):
        now = datetime.now().isoformat(" ").split(".")[0]
        print(f"{hitam}[{now}]{reset} {message}")

    def get_local_token(self, userid):
        if not os.path.exists("tokens.json"):
            open("tokens.json", "w").write(json.dumps({}))
        tokens = json.loads(open("tokens.json", "r").read())
        if str(userid) not in tokens.keys():
            return False

        return tokens[str(userid)]

    def save_local_token(self, userid, token):
        tokens = json.loads(open("tokens.json", "r").read())
        tokens[str(userid)] = token
        open("tokens.json", "w").write(json.dumps(tokens, indent=4))

    def is_expired(self, token):
        if token is None or isinstance(token, bool):
            return True
        header, payload, sign = token.split(".")
        payload = b64decode(payload + "==").decode()
        jload = json.loads(payload)
        now = round(datetime.now().timestamp()) + 300
        exp = jload["exp"]
        if now > exp:
            return True

        return False

    def save_failed_token(self, userid, data):
        file = "auth_failed.json"
        if not os.path.exists(file):
            open(file, "w").write(json.dumps({}))

        acc = json.loads(open(file, "r").read())
        if str(userid) in acc.keys():
            return

        acc[str(userid)] = data
        open(file, "w").write(json.dumps(acc, indent=4))

    def load_config(self):
        try:
            config = json.loads(open("config.json", "r").read())
            self.AUTOTASK = config["auto_complete_task"]
            self.AUTOGAME = config["auto_play_game"]
            self.DEFAULT_INTERVAL = config["interval"]
            self.MIN_WIN = config["game_point"]["low"]
            self.MAX_WIN = config["game_point"]["high"]
            if self.MIN_WIN > self.MAX_WIN:
                self.log(f"{kuning}high value must be higher than lower value")
                sys.exit()
        except json.decoder.JSONDecodeError:
            self.log(f"{merah}failed decode config.json")
            sys.exit()

    def ipinfo(self):
        res = self.http("https://ipinfo.io/json", {"content-type": "application/json"})
        if res is False:
            return False
        if res.status_code != 200:
            self.log(f"{merah}failed fetch ipinfo !")
            return False
        city = res.json().get("city")
        country = res.json().get("country")
        region = res.json().get("region")
        self.log(
            f"{hijau}country : {putih}{country} {hijau}region : {putih}{region} {hijau}city : {putih}{city}"
        )
        return True

    def http(self, url, headers, data=None):
        while True:
            try:
                logfile = "http.log"
                if not os.path.exists(logfile):
                    open(logfile, "a")
                logsize = os.path.getsize(logfile)
                if (logsize / 1024 / 1024) > 1:
                    open(logfile, "w").write("")
                if data is None:
                    res = self.ses.get(url, headers=headers, timeout=30)
                elif data == "":
                    res = self.ses.post(url, headers=headers, timeout=30)
                else:
                    res = self.ses.post(url, headers=headers, data=data, timeout=30)
                open(logfile, "a", encoding="utf-8").write(res.text + "\n")
                if "<title>" in res.text:
                    self.log(f"{merah}failed fetch json response !")
                    time.sleep(2)
                    continue

                return res

            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
                self.log(f"{merah}connection error/ connection timeout !")

            except requests.exceptions.ProxyError:
                self.log(f"{merah}bad proxy")
                return False

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
{magenta}┏┓┳┓┏┓  ┏┓    •      {putih}BlumTod Auto Claim for {hijau}blum
{magenta}┗┓┃┃┗┓  ┃┃┏┓┏┓┓┏┓┏╋  {hijau}Author : {putih}AkasakaID
{magenta}┗┛┻┛┗┛  ┣┛┛ ┗┛┃┗ ┗┗  {putih}Github : {hijau}https://github.com/AkasakaID
{magenta}              ┛      {hijau}Note : {putih}Every Action Has a Consequence
        """
        arg = argparse.ArgumentParser()
        arg.add_argument(
            "--marinkitagawa", action="store_true", help="no clear the terminal !"
        )
        arg.add_argument(
            "--data", help="Custom data input (default: data.txt)", default="data.txt"
        )
        arg.add_argument(
            "--proxy",
            help="custom proxy file input (default: proxies.txt)",
            default="proxies.txt",
        )
        args = arg.parse_args()
        if not args.marinkitagawa:
            os.system("cls" if os.name == "nt" else "clear")

        print(banner)
        if not os.path.exists(args.data):
            self.log(f"{merah}{args.data} not found, please input valid file name !")
            sys.exit()

        datas = [i for i in open(args.data, "r").read().splitlines() if len(i) > 0]
        proxies = [i for i in open(args.proxy).read().splitlines() if len(i) > 0]
        use_proxy = True if len(proxies) > 0 else False
        self.log(f"{hijau}total account : {putih}{len(datas)}")
        self.log(f"{biru}use proxy : {putih}{use_proxy}")
        if len(datas) <= 0:
            self.log(f"{merah}add data account in {args.data} first")
            sys.exit()
        print(self.garis)
        while True:
            list_countdown = []
            for no, data in enumerate(datas):
                self.log(f"{hijau}account number - {putih}{no + 1}")
                data_parse = self.data_parsing(data)
                user = json.loads(data_parse["user"])
                userid = user["id"]
                self.log(f"{hijau}login as : {putih}{user['first_name']}")
                if use_proxy:
                    proxy = proxies[no % len(proxies)]
                self.set_proxy(proxy if use_proxy else None)
                self.ipinfo() if use_proxy else None
                access_token = self.get_local_token(userid)
                failed_fetch_token = False
                while True:
                    if not access_token:
                        access_token = self.renew_access_token(data)
                        if not access_token:
                            self.save_failed_token(userid, data)
                            failed_fetch_token = True
                            break
                        self.save_local_token(userid, access_token)
                    expired = self.is_expired(access_token)
                    if expired:
                        access_token = False
                        continue
                    break
                if failed_fetch_token:
                    continue
                self.checkin(access_token)
                self.get_friend(access_token)
                if self.AUTOTASK:
                    self.solve_task(access_token)
                status, res_bal = self.get_balance(access_token)
                if status:
                    self.claim_farming(access_token)
                    res_bal = self.start_farming(access_token)
                if isinstance(res_bal, str):
                    res_bal = self.start_farming(access_token)
                list_countdown.append(res_bal)
                if self.AUTOGAME:
                    while True:
                        result = self.playgame(access_token)
                        if result:
                            access_token = self.renew_access_token(data)
                            self.save_local_token(userid, access_token)
                            continue
                        break
                print(self.garis)
                self.countdown(self.DEFAULT_INTERVAL)
            min_countdown = min(list_countdown)
            now = int(time.time())
            result = min_countdown - now
            if result <= 0:
                continue

            self.countdown(result)


if __name__ == "__main__":
    try:
        app = BlumTod()
        app.load_config()
        app.main()
    except KeyboardInterrupt:
        sys.exit()
