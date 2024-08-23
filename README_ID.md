# BlumTod

AUTO CLAIM FOR BLUM / @blum

# Daftar Isi
- [BlumTod](#blumtod)
- [Daftar Isi](#daftar-isi)
- [Peringatan](#peringatan)
- [Fitur yang tersedia.](#fitur-yang-tersedia)
- [Pendaftar](#pendaftar)
- [Cara Pemakaian](#cara-pemakaian)
  - [Bot.py Argumen](#botpy-argumen)
  - [Tentang Config.json](#tentang-configjson)
  - [Tentang Proxy](#tentang-proxy)
  - [Windows](#windows)
  - [Linux](#linux)
  - [Termux](#termux)
- [Cara Mendapatkan Query](#cara-mendapatkan-query)
- [Kode Javascript untuk Mendapatkan Data di Aplikasi Telegram Desktop](#kode-javascript-untuk-mendapatkan-data-di-aplikasi-telegram-desktop)
- [Menjalankan Selama 24/7](#menjalankan-selama-247)
- [Diskusi](#diskusi)
- [Dukung Hasil Pekerjaan Saya !](#dukung-hasil-pekerjaan-saya-)
- [Pertanyaan  dan Jawaban](#pertanyaan--dan-jawaban)
- [Terima Kasih](#terima-kasih)

# Peringatan

Segala risiko ditanggung oleh pemakai

# Fitur yang tersedia.

- [x] Otomatis Klaim Setiap 8 Jam
- [x] Otomatis CheckIn Harian (Login)
- [x] Otomatis Klaim Hasil Referral
- [x] Mendukung Penggunaan Proxy
- [x] Otomatis Menyelesaikan Tugas (Task)
- [x] Otomatis Bermain Game setelah Klaim 

# Pendaftar

Klik Tautan Berikut Untuk Melakukan Pendaftaran : [https://t.me/BlumCryptoBot/app?startapp=ref_aPYIYj1oKc](https://t.me/BlumCryptoBot/app?startapp=ref_aPYIYj1oKc)

# Cara Pemakaian

## Bot.py Argumen

| Nama Argument | Deskripsi                                                                          |
| ------------- | ---------------------------------------------------------------------------------- |
| --data        | Melakukan kustomisasi input file data / <br>query, secara bawaan adalah (data.txt) |
| --proxy       | Melakukan kustomisaasi input file proxy, secara bawaan adalah (proxies.txt)        |

## Tentang Config.json

Berikut adalah penjelasan tentang Nama (Key) dan Isi (Value) di dalam file config.json

| Nama (Key)         | Isi (Value)                                  | Deskripsi                                                                                                                                                                                                                                                   |
| ------------------ | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| interval           | Angka Positif ( 1 - 9999)                    | Berfungsi untuk nilai jeda antara akun                                                                                                                                                                                                                      |
| auto_complete_task | Boolean ( true (aktif) / false (non-aktif) ) | Berfungsi untuk meng-aktifkan dan <br>meng-non-aktifkan fitur Otomatis Penyelesaiian Task                                                                                                                                                                   |
| auto_play_game     | Boolean ( true (aktif) / false (non-aktif))  | Berfungsi untuk meng-aktifkan dan <br>meng-non-aktifkan fitur Otomatis Memaikan game                                                                                                                                                                        |
| game_point         | Angka Positif ( 1 - 9999)                    | game_point mempunyai sub key bernama low dan high. Berfungsi untuk melakukan kustomisasi point game <br>low adalahnilai paling rendah yang akan didapatkan ketika bermain game<br> high adalah nilai paling tinggi yang akan didapatkan ketika bermain game |

## Tentang Proxy

Daftar di Website Berikut untuk Mendapatkan Proxy Gratis : [Here](https://www.webshare.io/?referral_code=dwj0m9cdi4mp)

Anda bisa menambahkan daftar proxy di file `proxies.txt` dan format proxynya seprti berikut :

Format :

```
http://host:port
http://user:pass@host:port
```

Contoh :

```
http://127.0.0.1:6969
http://user:pass@127.0.0.1:6969
socks5://127.0.0.1:6969
socks5://user:pass@127.0.0.1:6969
```

## Windows 

1. Pastikan komputer anda telah terinstall python dan git.

    Saran: Gunakan python versi 3.8+ (3.8 keatas atau terbaru)
   
   python site : [https://python.org](https://python.org)
   
   git site : [https://git-scm.com/](https://git-scm.com/)

2. Clone / Duplikasi repository ini.
   ```shell
   git clone https://github.com/akasakaid/blumtod.git
   ```

3. Masuk ke folder BlumTod
   ```
   cd blumtod
   ```

4. Install module / library yang dibutuhkan.
   ```
   python -m pip install -r requirements.txt
   ```

5. Edit / ubah file `data.txt`, masukkan data query ke dalam file `data.txt`. Anda bisa mendapatkan query anda dengan cara [Cara Mendapatkan Query](#cara-mendapatkan-query). Satu baris untuk 1 akun, jika anda ingin menambah akun ke-2 maka isi di baris yang baru.

6. Jalankan program / scriptnya.
   ```
   python bot.py
   ```

## Linux 

1. Pastikan komputer anda telah terinstall python dan git.

    Saran: Gunakan python versi 3.8+ (3.8 keatas atau terbaru)
   
   python
   ```shell
   sudo apt install python3 python3-pip
   ```
   git
   ```shell
   sudo apt install git
   ```

2. Clone / Duplikasi repository ini.
   ```shell
   git clone https://github.com/akasakaid/blumtod.git
   ```

3. Masuk ke folder BlumTod
   ```
   cd blumtod
   ```

4. Install module / library yang dibutuhkan.
   ```
   python -m pip install -r requirements.txt
   ```

5. Edit / ubah file `data.txt`, masukkan data query ke dalam file `data.txt`. Anda bisa mendapatkan query anda dengan cara [Cara Mendapatkan Query](#cara-mendapatkan-query). Satu baris untuk 1 akun, jika anda ingin menambah akun ke-2 maka isi di baris yang baru.

6. Jalankan program / scriptnya.
   ```
   python bot.py
   ```

## Termux

1. Pastikan komputer anda telah terinstall python dan git.

    Saran: Gunakan python versi 3.8+ (3.8 keatas atau terbaru)
   
   python
   ```shell
   pkg install python3
   ```
   git
   ```shell
   pkg install git
   ```

2. Clone / Duplikasi repository ini.
   ```shell
   git clone https://github.com/akasakaid/blumtod.git
   ```

3. Masuk ke folder BlumTod
   ```
   cd blumtod
   ```

4. Install module / library yang dibutuhkan.
   ```
   python -m pip install -r requirements.txt
   ```

5. Edit / ubah file `data.txt`, masukkan data query ke dalam file `data.txt`. Anda bisa mendapatkan query anda dengan cara [Cara Mendapatkan Query](#cara-mendapatkan-query). Satu baris untuk 1 akun, jika anda ingin menambah akun ke-2 maka isi di baris yang baru.

6. Jalankan program / scriptnya.
   ```
   python bot.py
   ```


# Cara Mendapatkan Query

Data yang dibutuhkan sama seperti [pixelversebot](https://github.com/akasakaid/pixelversebot) jadi anda bisa menonton video panduan yang sama !

Berikut : [https://youtu.be/KTZW9A75guI](https://youtu.be/KTZW9A75guI)

# Kode Javascript untuk Mendapatkan Data di Aplikasi Telegram Desktop

```javascript
copy(Telegram.WebApp.initData)
```

# Menjalankan Selama 24/7

Anda bisa menjalankan script bot dalam 24/7 menggunakan vps / rdp. Anda bisa menggunakan aplikasi `screen` jika menggunakan sistem operasi linux untuk menjalakan script botnya di latar belakang.

# Diskusi

Jika anda memiliki pertanyaan atau yang lain, anda bisa bertanya disini : [@sdsproject_chat](https://t.me/sdsproject_chat)

# Dukung Hasil Pekerjaan Saya !

Jika anda suka dengan hasil pekerjaan saya anda bisa mendukung saya melakui tautan dibawah

- [Indonesia] https://s.id/nusanqr (QRIS)
- [Indonesia] https://trakteer.id/fawwazthoerif/tip
- [Global] https://sociabuzz.com/fawwazthoerif/tribe
- Jika anda ingin mengirim dalam bentuk lain, anda bisa menghubungi saya melalui telegram.

# Pertanyaan  dan Jawaban

Q : Apakah script bot / program ini wajib memaki proxy?

A : Tidak, script bot / program ini tidak wajib memakai proxy.

Q : Bagaimana cara saya memakai proxy?

A : Poenjelasan mudahnya anda cukup mengisi file `proxies.txt` dengan format proxy yang telah saya terangkan diatas .


# Terima Kasih 