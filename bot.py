import os
import sys
import json
import anyio
import httpx
import random
import asyncio
import argparse
import httpx_socks
from base64 import b64decode
from datetime import datetime
from urllib.parse import parse_qs
from fake_useragent import UserAgent
from colorama import init, Fore, Style


init(autoreset=True)
red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
black = Fore.LIGHTBLACK_EX
white = Fore.LIGHTWHITE_EX
reset = Style.RESET_ALL
magenta = Fore.LIGHTMAGENTA_EX
line = white + "~" * 50
log_file = "http.log"
proxy_file = "proxies.txt"
data_file = "data.txt"
config_file = "config.json"

with open(config_file, "r") as r:
    config = json.loads(r.read())
    auto_claim = config.get("auto_claim")
    auto_task = config.get("auto_task")
    auto_game = config.get("auto_game")
    low_game_point = config.get("low")
    high_game_point = config.get("high")
    low_countdown = config.get("clow")
    high_countdown = config.get("chigh")


class BlumTod:
    def __init__(self, id, query, proxies):
        self.p = id
        self.query = query
        self.proxies = proxies
        self.valid = True
        parser = {key: value[0] for key, value in parse_qs(query).items()}
        user = parser.get("user")
        if user is None:
            self.valid = False
            self.log(f"{red}this account data has the wrong format.")
            return None
        self.user = json.loads(user)
        proxy = (
            None if len(self.proxies) <= 0 else self.proxies[self.p % len(self.proxies)]
        )
        self.ses = httpx.AsyncClient(proxy=proxy, timeout=1000)
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/json",
            "lang": "en",
            "origin": "https://telegram.blum.codes",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "sec-ch-ua": '"Microsoft Edge WebView2";v="135", "Chromium";v="135", "Not-A.Brand";v="8", "Microsoft Edge";v="135"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0",
        }

    def log(self, msg):
        now = datetime.now().isoformat().split("T")[1].split(".")[0]
        print(
            f"{black}[{now}]{white}-{blue}[{white}acc {self.p + 1}{blue}]{white} {msg}{reset}"
        )

    async def ipinfo(self):
        ipinfo1_url = "https://ipapi.co/json/"
        ipinfo2_url = "https://ipwho.is/"
        ipinfo3_url = "https://freeipapi.com/api/json"
        headers = {"user-agent": "marin kitagawa"}
        try:
            res = await self.ses.get(ipinfo1_url)
            ip = res.json().get("ip")
            country = res.json().get("country")
            if not ip:
                res = await self.ses.get(ipinfo2_url)
                ip = res.json().get("ip")
                country = res.json().get("country_code")
                if not ip:
                    res = await self.ses.get(ipinfo3_url)
                    ip = res.json().get("ipAddress")
                    country = res.json().get("countryCode")
            self.log(f"{green}ip : {white}{ip} {green}country : {white}{country}")
        except json.decoder.JSONDecodeError:
            self.log(f"{green}ip : {white}None {green}country : {white}None")

    async def http(self, url, headers, data=None):
        while True:
            try:
                if (
                    not os.path.exists("http.log")
                    or os.path.getsize("http.log") / 1024 >= 2048
                ):
                    open("http.log", "a")
                if data is None:
                    res = await self.ses.get(url, headers=headers)
                elif data == "":
                    res = await self.ses.post(url, headers=headers)
                else:
                    res = await self.ses.post(url, headers=headers, data=data)
                open("http.log", "a", encoding="utf-8").write(
                    f"{res.status_code} {res.text}\n"
                )
                if "<title>" in res.text:
                    self.log(f"{yellow}failed get json response !")
                    await countdown(3)
                    continue
                return res
            except httpx.ProxyError:
                proxy = (
                    None
                    if len(self.proxies) <= 0
                    else self.proxies[
                        random.randint(1, len(self.proxies) - 1) % len(self.proxies)
                    ]
                )
                self.ses = httpx.AsyncClient(proxy=proxy)
                self.log(f"{yellow}proxy error,selecting random proxy !")
                await asyncio.sleep(3)
                continue
            except httpx.NetworkError:
                self.log(f"{yellow}network error !")
                await asyncio.sleep(3)
                continue
            except httpx.TimeoutException:
                self.log(f"{yellow}connection timeout !")
                await asyncio.sleep(3)
                continue
            except (httpx.RemoteProtocolError, anyio.EndOfStream):
                self.log(f"{yellow}connection close without response !")
                await asyncio.sleep(3)
                continue

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

    async def login(self):
        auth_url = "https://auth-domain.blum.codes/api/v1/auth"
        data = {
            "provider": "TELEGRAM",
            "strategy": "TELEGRAM",
            "payload": {"initData": self.query},
        }
        # print(data)
        res = await self.http(auth_url, self.headers, json.dumps(data))
        token = res.json().get("token")
        if not token:
            message = res.json().get("message", "")
            if "signature is invalid" in message:
                self.log(f"{red}data has the wrong format or data is outdated.")
                return False
            self.log(f"{red}{message}, check log file http.log !")
            return False
        token = token.get("access")
        self.log(f"{green}success get access token !")
        self.headers["authorization"] = f"Bearer {token}"
        return True

    async def checkin(self):
        url = "https://game-domain.blum.codes/api/v2/daily-reward"
        res = await self.http(url=url, headers=self.headers)
        today_reward = res.json().get("todayReward", {}).get("points")
        is_claim = res.json().get("claim")
        if is_claim == "unavailable":
            self.log(f"{yellow}already checkin today !")
            return False
        res = await self.http(url=url, headers=self.headers, data="")
        claimed = res.json().get("claimed")
        if claimed:
            self.log(f"{green}success checkin today,reward : {white}{today_reward}")
            return True

    async def start(self):
        rtime = random.randint(int(low_countdown), int(high_countdown))
        await countdown(rtime)
        if not self.valid:
            return int(datetime.now().timestamp()) + (3600 * 8)
        balance_url = "https://game-domain.blum.codes/api/v1/user/balance"
        friend_balance_url = "https://user-domain.blum.codes/api/v1/friends/balance"
        farming_claim_url = "https://game-domain.blum.codes/api/v1/farming/claim"
        farming_start_url = "https://game-domain.blum.codes/api/v1/farming/start"
        await self.ipinfo()
        uid = self.user.get("id")
        first_name = self.user.get("first_name")
        self.log(f"{green}login as {white}{first_name}")
        result = await self.login()
        if not result:
            return int(datetime.now().timestamp()) + 300
        await self.checkin()
        while True:
            res = await self.http(balance_url, self.headers)
            timestamp = res.json().get("timestamp")
            if timestamp == 0:
                timestamp = int(datetime.now().timestamp() * 1000)
            if not timestamp:
                continue
            timestamp = timestamp / 1000
            break
        balance = res.json().get("availableBalance", 0)
        farming = res.json().get("farming")
        end_iso = datetime.now().isoformat(" ")
        end_farming = int(datetime.now().timestamp() * 1000) + random.randint(
            3600000, 7200000
        )
        self.log(f"{green}balance : {white}{balance}")
        refres = await self.http(friend_balance_url, self.headers)
        amount_claim = refres.json().get("amountForClaim")
        can_claim = refres.json().get("canClaim", False)
        self.log(f"{green}referral balance : {white}{amount_claim}")
        if can_claim:
            friend_claim_url = "https://user-domain.blum.codes/api/v1/friends/claim"
            clres = await self.http(friend_claim_url, self.headers, "")
            if clres.json().get("claimBalance") is not None:
                self.log(f"{green}success claim referral reward !")
            else:
                self.log(f"{red}failed claim referral reward !")
        if auto_claim:
            while True:
                if farming is None:
                    _res = await self.http(farming_start_url, self.headers, "")
                    if _res.status_code != 200:
                        self.log(f"{red}failed start farming !")
                    else:
                        self.log(f"{green}success start farming !")
                        farming = _res.json()
                if farming is None:
                    res = await self.http(balance_url, self.headers)
                    farming = res.json().get("farming")
                    if farming is None:
                        continue
                end_farming = farming.get("endTime")
                if timestamp > (end_farming / 1000):
                    res_ = await self.http(farming_claim_url, self.headers, "")
                    if res_.status_code != 200:
                        self.log(f"{red}failed claim farming !")
                    else:
                        self.log(f"{green}success claim farming !")
                        farming = None
                        continue
                else:
                    self.log(f"{yellow}not time to claim farming !")
                end_iso = (
                    datetime.fromtimestamp(end_farming / 1000)
                    .isoformat(" ")
                    .split(".")[0]
                )
                break
            self.log(f"{green}end farming : {white}{end_iso}")
        if auto_task:
            task_url = "https://earn-domain.blum.codes/api/v1/tasks"
            res = await self.http(task_url, self.headers)
            for tasks in res.json():
                if isinstance(tasks, str):
                    self.log(f"{yellow}failed get task list !")
                    break
                for k in list(tasks.keys()):
                    if k != "tasks" and k != "subSections":
                        continue
                    for t in tasks.get(k):
                        if isinstance(t, dict):
                            subtasks = t.get("subTasks")
                            if subtasks is not None:
                                for task in subtasks:
                                    await self.solve(task)
                                await self.solve(t)
                                continue
                        _tasks = t.get("tasks")
                        if not _tasks:
                            continue
                        for task in _tasks:
                            await self.solve(task)
        if auto_game:
            play_url = "https://game-domain.blum.codes/api/v2/game/play"
            claim_url = "https://game-domain.blum.codes/api/v2/game/claim"
            game = True
            while game:
                res = await self.http(balance_url, self.headers)
                play = res.json().get("playPasses")
                if play is None:
                    self.log(f"{yellow}failed get game ticket !")
                    break
                self.log(f"{green}you have {white}{play}{green} game ticket")
                if play <= 0:
                    break
                for i in range(play):
                    if self.is_expired(self.headers.get("authorization").split(" ")[1]):
                        result = await self.login()
                        if not result:
                            break
                        continue
                    res = await self.http(play_url, self.headers, "")
                    game_id = res.json().get("gameId")
                    if game_id is None:
                        message = res.json().get("message", "")
                        if message == "cannot start game":
                            self.log(f"{yellow}{message}")
                            game = False
                            break
                        self.log(f"{yellow}{message}")
                        continue
                    while True:
                        await countdown(35)
                        point = random.randint(
                            int(low_game_point), int(high_game_point)
                        )
                        freeze = random.randint(1, 2)
                        data = json.dumps(
                            {"game_id": game_id, "points": point, "freeze": freeze}
                        )
                        _headers = {
                            "User-Agent": UserAgent().random,
                            "Content-Type": "application/json",
                        }
                        res = await self.http(
                            url="https://blum-payload.sdsproject.org",
                            headers=_headers,
                            data=data,
                        )
                        data = res.text
                        res = await self.http(claim_url, self.headers, data)
                        if "OK" in res.text:
                            self.log(
                                f"{green}success earn {white}{point}{green} from game !"
                            )
                            break
                        message = res.json().get("message", "")
                        if message == "game session not finished":
                            continue
                        self.log(f"{red}failed earn {white}{point}{red} from game !")
                        break
        res = await self.http(balance_url, self.headers)
        balance = res.json().get("availableBalance", 0)
        self.log(f"{green}balance :{white}{balance}")
        return round(end_farming / 1000)

    async def solve(self, task):
        task_id = task.get("id")
        task_title = task.get("title")
        task_status = task.get("status")
        task_type = task.get("type")
        validation_type = task.get("validationType")
        start_task_url = f"https://earn-domain.blum.codes/api/v1/tasks/{task_id}/start"
        claim_task_url = f"https://earn-domain.blum.codes/api/v1/tasks/{task_id}/claim"
        while True:
            if task_status == "FINISHED":
                self.log(f"{yellow}already complete task id {white}{task_id} !")
                return
            if task_status == "READY_FOR_CLAIM" or task_status == "STARTED":
                _res = await self.http(claim_task_url, self.headers, "")
                message = _res.json().get("message")
                if message:
                    return
                _status = _res.json().get("status")
                if _status == "FINISHED":
                    self.log(f"{green}success complete task id {white}{task_id} !")
                    return
            if task_status == "NOT_STARTED" and task_type == "PROGRESS_TARGET":
                return
            if task_status == "NOT_STARTED":
                _res = await self.http(start_task_url, self.headers, "")
                await countdown(3)
                message = _res.json().get("message")
                if message:
                    return
                task_status = _res.json().get("status")
                continue
            if validation_type == "KEYWORD" or task_status == "READY_FOR_VERIFY":
                verify_url = (
                    f"https://earn-domain.blum.codes/api/v1/tasks/{task_id}/validate"
                )
                answer_url = "https://akasakaid.github.io/blum/answer.json"
                res_ = await self.http(answer_url, {"User-Agent": "Marin Kitagawa"})
                answers = res_.json()
                answer = answers.get(task_id)
                if not answer:
                    self.log(f"{yellow}answers to quiz tasks are not yet available.")
                    return
                data = {"keyword": answer}
                res = await self.http(verify_url, self.headers, json.dumps(data))
                message = res.json().get("message")
                if message:
                    return
                task_status = res.json().get("status")
                continue
            return


async def countdown(t):
    for i in range(t, 0, -1):
        minute, seconds = divmod(i, 60)
        hour, minute = divmod(minute, 60)
        seconds = str(seconds).zfill(2)
        minute = str(minute).zfill(2)
        hour = str(hour).zfill(2)
        print(f"waiting for {hour}:{minute}:{seconds} ", flush=True, end="\r")
        await asyncio.sleep(1)


async def main():
    global \
        auto_claim, \
        auto_task, \
        auto_game, \
        high_game_point, \
        low_game_point, \
        high_countdown, \
        low_countdown
    banner = f"""
{magenta}┏┓┳┓┏┓  ┏┓    •      {white}BlumTod Auto Claim for {green}blum
{magenta}┗┓┃┃┗┓  ┃┃┏┓┏┓┓┏┓┏╋  {green}Author : {white}AkasakaID
{magenta}┗┛┻┛┗┛  ┣┛┛ ┗┛┃┗ ┗┗  {white}Github : {green}https://github.com/AkasakaID
{magenta}              ┛      {green}Note : {white}Every Action Has a Consequence
        """
    arg = argparse.ArgumentParser()
    arg.add_argument(
        "--data",
        "-D",
        default=data_file,
        help=f"Perform custom input for data files (default: {data_file})",
    )
    arg.add_argument(
        "--proxy",
        "-P",
        default=proxy_file,
        help=f"Perform custom input for proxy files (default : {proxy_file})",
    )
    arg.add_argument(
        "--action",
        "-A",
        help="Function to directly enter the menu without displaying input",
    )
    arg.add_argument(
        "--worker",
        "-W",
        help="Total workers or number of threads to be used (default : cpu core / 2)",
    )
    arg.add_argument("--marin", action="store_true")
    args = arg.parse_args()
    if not os.path.exists(args.data):
        open(args.data, "a")
    if not os.path.exists(args.proxy):
        open(args.proxy, "a")
    if not os.path.exists(config_file):
        with open("config.json", "w") as w:
            _config = {
                "auto_claim": True,
                "auto_task": True,
                "auto_game": True,
                "low": 240,
                "high": 250,
                "clow": 30,
                "chigh": 60,
            }
            w.write(json.dumps(_config, indent=4))
    while True:
        if not args.marin:
            os.system("cls" if os.name == "nt" else "clear")
        print(banner)
        datas = open(args.data).read().splitlines()
        proxies = open(args.proxy).read().splitlines()

        menu = f"""
{white}data file :{green} {args.data}
{white}proxy file :{green} {args.proxy}
{green}total data :{white} {len(datas)}
{green}total proxy :{white} {len(proxies)}

    {green}1{white}.{green}) {white}set on/off auto claim ({(green + "active" if auto_claim else red + "non-active")})
    {green}2{white}.{green}) {white}set on/off auto solve task ({(green + "active" if auto_task else red + "non-active")})
    {green}3{white}.{green}) {white}set on/off auto play game ({(green + "active" if auto_game else red + "non-active")})
    {green}4{white}.{green}) {white}set game point {green}({low_game_point}-{high_game_point})
    {green}5{white}.{green}) {white}set wait time before start {green}({low_countdown}-{high_countdown})
    {green}6{white}.{green}) {white}start bot (multiprocessing)
    {green}7{white}.{green}) {white}start bot (sync mode)
        """
        opt = None
        if args.action:
            opt = args.action
        else:
            print(menu)
            opt = input(f"{green}input number : {white}")
            print(f"{white}~" * 50)
        if opt == "1":
            config["auto_claim"] = False if auto_claim else True
            auto_claim = False if auto_claim else True
            with open(config_file, "w") as w:
                w.write(json.dumps(config, indent=4))
            print(f"{green}success update auto claim config")
            input(f"{blue}press enter to continue")
            opt = None
            continue
        if opt == "2":
            config["auto_task"] = False if auto_task else True
            auto_task = False if auto_task else True
            with open(config_file, "w") as w:
                w.write(json.dumps(config, indent=4))
            print(f"{green}success update auto task config !")
            input(f"{blue}press enter to continue")
            opt = None
            continue
        if opt == "3":
            config["auto_game"] = False if auto_game else True
            auto_game = False if auto_game else True
            with open(config_file, "w") as w:
                w.write(json.dumps(config, indent=4))
            print(f"{green}success update auto game config !")
            input(f"{blue}press enter to continue")
            opt = None
            continue
        if opt == "4":
            low = input(f"{green}input low game point : {white}") or 240
            high = input(f"{green}input high game point : {white}") or 250
            config["low"] = low
            config["high"] = high
            low_game_point = low
            high_game_point = high
            with open(config_file, "w") as w:
                w.write(json.dumps(config, indent=4))

            print(f"{green}success update game point !")
            input(f"{blue}press enter to continue")
            opt = None
            continue
        if opt == "6":
            if not args.worker:
                worker = int(os.cpu_count() / 2)
                if worker < 1:
                    worker = 1
            else:
                worker = int(args.worker)
            sema = asyncio.Semaphore(worker)

            async def bound(sem, params):
                async with sem:
                    return await BlumTod(*params).start()

            while True:
                tasks = [
                    asyncio.create_task(bound(sema, (no, data, proxies)))
                    for no, data in enumerate(datas)
                ]
                result = await asyncio.gather(*tasks)
                end = int(datetime.now().timestamp())
                total = min(result) - end
                await countdown(total)
        if opt == "7":
            while True:
                result = []
                for no, data in enumerate(datas):
                    res = await BlumTod(id=no, query=data, proxies=proxies).start()
                    result.append(res)
                end = int(datetime.now().timestamp())
                total = min(result) - end
                await countdown(total)
        if opt == "5":
            low = input(f"{green}input low wait time : {white}") or 30
            high = input(f"{green}input high wait time : {white}") or 60
            config["clow"] = low
            config["chigh"] = high
            low_countdown = low
            high_countdown = high
            with open(config_file, "w") as w:
                w.write(json.dumps(config, indent=4))
            print(f"{green}success update wait time !")
            input(f"{blue}press enter to continue")
            opt = None
            continue


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, EOFError):
        sys.exit()
