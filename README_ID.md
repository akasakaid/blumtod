# BlumTod

AUTO CLAIM FOR BLUM / @blum

# Daftar Isi
- [BlumTod](#blumtod)
- [Daftar Isi](#daftar-isi)
- [Peringatan](#peringatan)
- [Dukung Hasil Pekerjaan Saya !](#dukung-hasil-pekerjaan-saya-)
- [Fitur yang tersedia.](#fitur-yang-tersedia)
- [Pendaftar](#pendaftar)
- [Cara Pemakaian](#cara-pemakaian)
  - [Opsi Command Line / Argument Command Line](#opsi-command-line--argument-command-line)
  - [Tentang Proxy](#tentang-proxy)
  - [Windows](#windows)
  - [Linux](#linux)
  - [Termux](#termux)
- [Melihat Laporan](#melihat-laporan)
- [Cara Mendapatkan Query](#cara-mendapatkan-query)
- [Kode Javascript untuk Mendapatkan Data di Aplikasi Telegram Desktop](#kode-javascript-untuk-mendapatkan-data-di-aplikasi-telegram-desktop)
- [Cara Melakukan Update](#cara-melakukan-update)
- [Menjalankan Selama 24/7](#menjalankan-selama-247)
- [Tabel Eror](#tabel-eror)
- [Diskusi](#diskusi)
- [Pertanyaan  dan Jawaban](#pertanyaan--dan-jawaban)
- [Terima Kasih](#terima-kasih)

# Peringatan

Segala risiko ditanggung oleh pemakai

# Dukung Hasil Pekerjaan Saya !

Jika anda suka dengan hasil pekerjaan saya anda bisa mendukung saya melakui tautan dibawah

- [Indonesia] https://s.id/nusanqr (QRIS)
- [Indonesia] https://trakteer.id/fawwazthoerif/tip
- [Global] https://sociabuzz.com/fawwazthoerif/tribe
- Jika anda ingin mengirim dalam bentuk lain, anda bisa menghubungi saya melalui telegram.

# Fitur yang tersedia.

- [x] Otomatis Klaim Setiap 8 Jam
- [x] Otomatis CheckIn Harian (Login)
- [x] Otomatis Klaim Hasil Referral
- [x] Mendukung Penggunaan Proxy
- [x] Otomatis Menyelesaikan Tugas (Task)
- [x] Otomatis Bermain Game setelah Klaim 
- [x] Mendukung multi proses
- [x] User-Agent acak
- [x] Laporan total saldo semua akun
- [x] Waktu tunggu sebelum memulai program

# Pendaftar

Klik Tautan Berikut Untuk Melakukan Pendaftaran : [https://t.me/BlumCryptoBot/app?startapp=ref_aPYIYj1oKc](https://t.me/BlumCryptoBot/app?startapp=ref_aPYIYj1oKc)

# Cara Pemakaian

## Opsi Command Line / Argument Command Line

Script / program ini juga mendukung beberapa argument parameter yang bisa dipakai, berikut adalah penjelasan argument 

`--data` / `-D` bisa digunakan ketika anda mempunyai nama file yang berbeda untuk menyimpan data akun. Secara bawaan nama file yang digunakan oleh script / program ini untuk menyimpan data akun adalah `data.txt`, semisal anda mempunyai file bernama `query.txt` sebagai file yang menyimpan data akun maka tinggal jalankan `bot.py` dengan menambahkan argumetn `--data` / `-D`. Contoh `python bot.py --data query.txt`

`--proxy` / `-P` bisa digunakan ketika anda mempunyai nama file yang berbeda untuk menyimpan list proxy. Nama file yang digunakan oleh script / program ini untuk menyimpan daftar proxy adalah `proxies.txt`, semisal anda mempunyai file bernama `prox.txt` sebagai file yang menyimpan daftar proxy, anda hanya tinggal menambahkan argument parameter `--proxy` / `-P` untuk dapat menggunakan file proxy anda. Contoh `python bot.py --proxy prox.txt`

`--worker` / `-W` argument ini berfungsi untuk melakukan kustomisasi jumlah thread / worker yang digunakan ketika script bot ini berjalan. Secara bawaan script / software ini jumlah worker nya adalah (total core cpu / 2), semisal cpu anda memiliki core 6 maka jumlah worker yang digunakan adalah 3. Anda bisa melakukan kustomisasi untuk jumlah worker ini menggunakan argument ini. Contohnya anda ingin membuat jumlah worker nya menjadi 100 maka jalankan `bot.py` dengan argument seperti ini `python bot.py --worker 100`. Dan jika anda tidak suka menggunakan worker / thread / multiprocessing maka anda bisa melakukan kustomisasi worker menjadi 1, contoh `python bot.py --worker 1`.

`--action` / `-A` argument ini berfungsi untuk langsung masuk ke kemu yang dituju, misal dalam script bot ini ada 5 menu jika anda tidak ingin melakukan input secara manual anda bisa menggunakan argument ini untuk langsung masuk ke menu yang dituju. Contoh : `python bot.py --action 5` dalalm contoh tersebut berarti anda akan langsung masuk ke menu nomor 5. Argument ini berguna jika kalian menggunakan docker / pm2 untuk menjalankan script bot di proses background.

## Tentang Proxy

Daftar di Website Berikut untuk Mendapatkan Proxy Gratis : [Here](https://www.webshare.io/?referral_code=dwj0m9cdi4mp)

Website dengan harga proxy termurah $1/GB [Here](https://dataimpulse.com/?aff=48082)

Anda bisa menambahkan daftar proxy di file `proxies.txt` dan format proxynya seprti berikut :

Jika terdapat autentikasi :

Format : 

```
protocol://user:password@hostname:port
```

Contoh :

```
http://admin:admin@69.69.69.69:6969
```

Jika tidak ada autentikasi :

Format :

```
protocol://hostname:port
```

Contoh :

```
```

Contoh :

```
http://69.69.69.69:6969
```

Tolong diperhatikan dengan saksama apakah proxy yang anda gunakan itu harus menggunakan autentikasi atau tidak, karena banyak orang yang DM saya bertanya cara penggunaan proxy.

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

# Melihat Laporan

Untuk melihat laporan total saldo semua akun anda dapat menjalankan file bernama `report.py`

```shell
python report.py
```


# Cara Mendapatkan Query

Data yang dibutuhkan sama seperti [pixelversebot](https://github.com/akasakaid/pixelversebot) jadi anda bisa menonton video panduan yang sama !

Berikut : [https://youtu.be/KTZW9A75guI](https://youtu.be/KTZW9A75guI)

# Kode Javascript untuk Mendapatkan Data di Aplikasi Telegram Desktop

Berikut beberapa kode javascript yang  bisa dicoba untuk mendapatkan data melalui aplikasi telegram desktop.

Setelah anda melakukan eksesusi kode coba melakukan paste jika tidak muncul maka coba kode javascript selainnya.

```javascript
copy(Telegram.WebApp.initData)
```

```javascript
copy(JSON.parse(sessionStorage.__telegram__initParams).tgWebAppData)
```

# Cara Melakukan Update

Hapus terlebih dahulu file `database.sqlite3`, anda bisa menggunakan peringah terminal dibawah (sesuaikan dengan sistem operasi yang anda gunakan)

Windows CMD / Windows Powershell

```shell
del database.sqlite3
```

Linux/Termux/Unix/MacOs

```shell
rm database.sqlite3
```

Anda bisa melakukan update hanya dengan perintah `git pull` jika anda memang dari awal sudah melakukan clone repository dengan git.
Jika anda tidak melakukan clone repository dengan git anda bisa melakukan update paksa dengan perintah dibawah (sesuaikan sistem operasi yang anda gunakan.).

Windows powershell : 
```shell
Invoke-WebRequest https://raw.githubusercontent.com/akasakaid/blumtod/refs/heads/main/bot.py -OutFile bot.py; Invoke-WebRequest https://raw.githubusercontent.com/akasakaid/blumtod/refs/heads/main/models.py -OutFile models.py; Invoke-WebRequest https://raw.githubusercontent.com/akasakaid/blumtod/refs/heads/main/requirements.txt -OutFile requirements.txt
```

Linux/Termux/Unix/Windows CMD/MacOS: 

```shell
curl https://raw.githubusercontent.com/akasakaid/blumtod/refs/heads/main/bot.py -o bot.py && curl https://raw.githubusercontent.com/akasakaid/blumtod/refs/heads/main/models.py -o models.py && curl https://raw.githubusercontent.com/akasakaid/blumtod/refs/heads/main/requirements.txt -o requirements.txt
```

# Menjalankan Selama 24/7

Anda bisa menjalankan script bot dalam 24/7 menggunakan vps / rdp. Anda bisa menggunakan aplikasi `screen` atau `pm2` jika menggunakan sistem operasi linux untuk menjalakan script botnya di latar belakang.

# Tabel Eror

| error                 | deskripsi                                                                                                                     |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| failed get json error | Ini dikarenakan respon server tidak berupa json dan mungkin berupa html, bisa kalian cek di file http.log untuk respon server |
| failed get task list  | Ini dikarenakan respon server tidak memberikan respon yang seharunya, bisa kalian cek di file http.log untuk respon server    |
| cannot start game     | Sama seperti error diatas, ini dikarenakan server. Kalian bisa cek di file http.log untuk respon server                       |

# Diskusi

Jika anda memiliki pertanyaan atau yang lain, anda bisa bertanya disini : [@sdsproject_chat](https://t.me/sdsproject_chat)

# Pertanyaan  dan Jawaban

Q : Apakah script bot / program ini wajib memaki proxy?

A : Tidak, script bot / program ini tidak wajib memakai proxy.

Q : Bagaimana cara saya memakai proxy?

A : Poenjelasan mudahnya anda cukup mengisi file `proxies.txt` dengan format proxy yang telah saya terangkan diatas .

# Terima Kasih 