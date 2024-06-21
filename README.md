# Blumtod

AUTO CLAIM FOR BLUM / @BlumCryptoBot

# Table of Contents
- [Blumtod](#blumtod)
- [Table of Contents](#table-of-contents)
- [Feature](#feature)
- [Register ?](#register-)
- [How to Use](#how-to-use)
  - [Bot.py parameter feature](#botpy-parameter-feature)
  - [Windows](#windows)
  - [Linux](#linux)
  - [Termux](#termux)
- [Config.json configuration](#configjson-configuration)
- [Play Game Configuration](#play-game-configuration)
- [Video Guide to Get Data](#video-guide-to-get-data)
- [Javascript Command to Get Telegram Data for Desktop](#javascript-command-to-get-telegram-data-for-desktop)
- [Run for 24/7](#run-for-247)
- [Discussion](#discussion)
- [Support](#support)
- [Thank you \< 3](#thank-you--3)

# Feature

- [x] Auto Claim
- [x] Auto Claim Daily
- [x] Support Multi Account
- [x] Auto Claim Bonus Referral
- [x] Auto Complete Task, see [Bot.py parameter feature](#botpy-parameter-feature)
- [x] Auto Play Game (random input from user), see [Play Game Configuration](#play-game-configuration)

# Register ?

My referral is full so i dont need referral again, ask u friend for invitation code !

# How to Use

## Bot.py parameter feature

Here are some parameters to enable feature

| parameter  | description                                    |
| ---------- | ---------------------------------------------- |
| --data     | set custom file data input (default: data.txt) |
| --autotask | to enable feature auto complete task           |
| --autogame | to enable feature auto playing game            |

## Windows 

1. Make sure you computer was installed python and git.
   
   python site : [https://python.org](https://python.org)
   
   git site : [https://git-scm.com/](https://git-scm.com/)

2. Clone this repository
   ```shell
   git clone https://github.com/akasakaid/blumtod.git
   ```

3. goto blumtod directory
   ```
   cd blumtod
   ```

4. install the require library
   ```
   python -m pip install -r requirements.txt
   ```

5. Edit `data.txt`, input you data token in `data.txt`, find you token in [How to Find Account Token](#how-to-find-account-token). One line for one data account, if you want add you second account add in new line!

6. execute the main program 
   ```
   python bot.py
   ```

## Linux

1. Make sure you computer was installed python and git.
   
   python
   ```shell
   sudo apt install python3 python3-pip
   ```
   git
   ```shell
   sudo apt install git
   ```

2. Clone this repository
   
   ```shell
   git clone https://github.com/akasakaid/blumtod.git
   ```

3. goto blumtod directory

   ```shell
   cd blumtod
   ```

4. Install the require library
   
   ```
   python3 -m pip install -r requirements.txt
   ```

5. Edit `data.txt`, input you data token in `data.txt`, find you token in [How to Find Account Token](#how-to-find-account-token). One line for one data account, if you want add you second account add in new line!

6. execute the main program 
   ```
   python bot.py
   ```

## Termux

1. Make sure you termux was installed python and git.
   
   python
   ```
   pkg install python
   ```

   git
   ```
   pkg install git
   ```

2. Clone this repository
   ```shell
   git clone https://github.com/akasakaid/blumtod.git
   ```

3. goto blumtod directory
   ```
   cd blumtod
   ```

4. install the require library
   ```
   python -m pip install -r requirements.txt
   ```

5. Edit `data.txt`, input you data token in `data.txt`, find you token in [How to Find Account Token](#how-to-find-account-token). One line for one data account, if you want add you second account add in new line!

6. execute the main program 
   ```
   python bot.py
   ```

# Config.json configuration

| Key      | value & description                                                   |
| -------- | --------------------------------------------------------------------- |
| interval | value can be inteter or float <br> interval is delay between accounts |

Example

```shell
python bot.py autotask autogame
```

# Play Game Configuration

Edit `config.json` to set your point that your want !

| Key        | Value and description                                                                                        |
| ---------- | ------------------------------------------------------------------------------------------------------------ |
| game_point | low : minimum points earned when playing the game <br><br>high : maximal points earned when playing the game |

# Video Guide to Get Data

The require data is same like [pixelversebot](https://github.com/akasakaid/pixelversebot) so you can watch same tutorial / video guide to get data !

Here : [https://youtu.be/KTZW9A75guI](https://youtu.be/KTZW9A75guI)

# Javascript Command to Get Telegram Data for Desktop

```javascript
copy(Telegram.WebApp.initData)
```

# Run for 24/7 

You can run the script bot for 24/7 using vps / rdp. You can use `screen` application in vps linux to running the script bot in background process

# Discussion

If you have an question or something you can ask in here : [@sdsproject_chat](https://t.me/sdsproject_chat)

# Support

To support me you can buy me a coffee via website in below

- https://trakteer.id/fawwazthoerif/tip
- https://sociabuzz.com/fawwazthoerif/tribe

# Thank you < 3