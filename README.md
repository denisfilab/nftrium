**Nama: Daanish Inayat Rahman**
**NPM: 2306213136**
**Kelas: PBP A**

# Link PWS

**http://daanish-inayat-nftriumm.pbp.cs.ui.ac.id/**

# Creating a new django project

Sebelum saya membuat django project, saya harus membuat environment untuk python terlebih dahulu, hal tersebut bisa dilakukan dengan run kode tersebut di terminal

```
env\Scripts\activate
```

Setelah virtual environment telah dibuat, saya perlu menginstall dependencies. Apa itu dependencies? library atau paket yang dibutuhkan agar suatu project bisa berjalan dengan lancar, hal ini bisa dilakukan dengan

```
python3 -m pip install django gunicorn whitenoise psycopg2-binary requests urllib3
```

atau package tersebut bisa dimasukkan ke requirements.txt dan melalkukan

```
python3 -m pip install requirements.txt
```

Setelah semua depedencies telah diintstall, saya membuat sebuah project django dengan menjalankan

```
django-admin startproject nftrium .
```

Setelah itu, saya membuat sebuah aplikasi bernama main dengan menjalankan

```
python3 manage.py startapp main
```

# Menambahkan 'main' di INSTALLED_APPS

Setelah itu, buka file `settings.py` yang ada di direktori proyekmu (misalnya di `nftrium/settings.py`), lalu tambahkan `'main'` di dalam variabel `INSTALLED_APPS` agar aplikasi kita terdaftar dan bisa digunakan. Ini contohnya:

```python
INSTALLED_APPS = [
    ...,
    'main',
]
```

# Membuat model NFT

Untuk membuat model NFT, kita perlu menggunakan beberapa library, yaitu `hashlib` untuk menghasilkan hash dan `uuid` untuk membuat ID unik. Kode berikut ini saya masukkan di file `models.py` di dalam direktori `main`

```python
import hashlib
import uuid
from django.db import models
class NFT(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='nfts/')
    creator = models.CharField(max_length=255)
    token_id = models.CharField(max_length=255, unique=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

# Memastikan Django Membaca Model dan App yang Baru Dibuat

Setelah membuat model dan app baru, kita perlu menjalankan perintah ini agar Django mengetahui perubahan yang telah kita lakukan dan menyimpannya ke dalam database. Langkah ini penting karena Django menggunakan sistem migrations untuk melacak dan menerapkan perubahan yang kita buat pada model.

### Langkah-langkah:

1. **Membuat migrations**:
   Jalankan perintah berikut untuk membuat file migrations yang mencatat perubahan pada model.
    ```bash
    python3 manage.py makemigrations
    ```
2. **Menerapkan migrations ke database**: Setelah migrations dibuat, gunakan perintah berikut untuk menerapkan perubahan tersebut ke dalam database.
    ```
    python3 manage.py migrate
    ```

# Membuat `views.py`

Di Django, `views.py` bertanggung jawab untuk mengambil data dari model dan meneruskannya ke template. Pada dasarnya, file `views.py` memungkinkan kita untuk mengirim variabel ke dalam template agar bisa digunakan di dalam HTML.

### Konteks:

Dalam kasus ini, kita akan mengambil data NFT dari database untuk disimpan dalam var `nfts` dan mengirimkannya ke template yang disebut `main.html` dan diteruskan ke `nftcard.html`. Template tersebut kemudian menggunakan informasi dari NFT tersebut untuk menampilkan data seperti nama, harga, deskripsi, dll. Setelah itu, template `nftcard.html` digunakan di dalam file `main.html` sebagai bagian dari komponen yang lebih besar.

### Kode di `views.py`:

```python
from django.shortcuts import render
from .models import NFT

def show_main(request):
    nfts = NFT.objects.all()  # Mengambil semua objek NFT dari database
    context = {
        'nfts': nfts  # Menyimpan data NFT ke dalam konteks
    }
    return render(request, "main.html", context)  # Mengirim konteks ke template 'main.html'
```

### Menampilkan di `main.html`

Setelah data NFT dikirim ke template main.html, kita bisa mengiterasi setiap NFT dan menampilkannya menggunakan komponen nftcard.html. Di sini kita menggunakan perulangan {% for %} untuk mengiterasi objek nfts, dan setiap objek dikirimkan ke nftcard.html.

```
{% for nft in nfts %}
    {% include 'components/nftcard.html' with nft=nft %}
{% endfor %}
```

### Komponen nftcard.html

Di dalam komponen ini, kita menerima objek nft yang dikirim dari `main.html`. Komponen ini mengakses class attribut yang dimiliki model tersebut dan menampilkannya.

# Menambahkan `URL_PATTERN` di urls.py projek

Untuk memastikan projek bisa memetakan template sesuai request user, kita harus menambahkan pattern url. Dalam konteks ini, kita perlu memetakan fungsi yang pernah kita buat yaitu `show_main`. Kita perlu memasukkan kode tersebut di urls.py di dalam variable `URL_PATTERN`.

```
path('', show_main, name='show_main'),
```

# Mengubah `ALLOWED_HOST`

Untuk menjalankan aplikasi Django di pws dan local, kita perlu mengatur variabel `ALLOWED_HOSTS` di file `settings.py`.

```
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "daanish-inayat-nftrium.pbp.cs.ui.ac.id"]
```

# Penjelasan request client ke web aplikasi berbasis Django

![Add a subheading](https://github.com/user-attachments/assets/e5b9f583-c38c-4e75-ae98-b4b350136b4f)

1. **Permintaan dari Client**:
   Pengguna mengakses URL (misalnya, `/products`) yang dikirim ke server Django.

2. **urls.py**:
   Pola URL dicocokkan dan diteruskan ke fungsi view yang sesuai.

3. **views.py**:
   View memproses permintaan, mungkin mengambil data dari database melalui `models.py`.

4. **models.py**:
   Jika diperlukan, data diambil dari database dan dikembalikan ke `views.py`.

5. **Rendering Template**:
   Data dari `views.py` diteruskan ke template HTML, lalu halaman dirender dan dikirim kembali ke client.

# Fungsi Git dalam Pengembangan Perangkat Lunak

Git sangat penting dalam pengembangan perangkat lunak karena memungkinkan banyak pengembang bekerja pada proyek yang sama secara bersamaan tanpa konflik. Dengan **branching**, setiap developer dapat fokus mengerjakan fitur atau perbaikan mereka sendiri. Setelah selesai, mereka bisa **push** perubahan dan membuat **pull request** agar kode tersebut direview oleh tim. Hal ini membantu menjaga kualitas kode melalui kolaborasi dan review.

Selain itu, Git memberikan **version control** yang sangat berguna. Jika ada pembaruan atau perubahan yang menyebabkan bug atau masalah, kita dapat dengan cepat **revert** ke versi sebelumnya, memastikan proyek tetap stabil dan bisa terus berkembang tanpa masalah besar.

# Mengapa Django Cocok sebagai Langkah Awal dalam Pembelajaran Pengembangan Perangkat Lunak?

Saya sudah pernah menggunakan **Next.js** sebelumnya, dan memang framework ini cukup luar biasa, terutama dalam pengembangan front-end. Di **Next.js**, banyak hal seperti pemanggilan API, koneksi ke database, dan pengambilan data sudah sangat disederhanakan. Semua terasa lebih mudah, hampir seperti bekerja dengan "kotak hitam" di mana kita hanya perlu mengikuti prosedur yang ada.

Namun, justru karena itulah saya merasa **Django** lebih cocok untuk pemula yang ingin mempelajari pengembangan perangkat lunak secara menyeluruh:

1. **Full-Stack Framework**: Django adalah framework full-stack yang berarti Django menangani semua aspek pengembangan aplikasi web, mulai dari front-end hingga back-end, termasuk database. Hal ini memberikan kesempatan bagi pemula untuk mempelajari seluruh _lifecycle_ pengembangan aplikasi dalam satu _framework_.

2. **Struktur yang Teratur**: Django menawarkan struktur yang sangat terorganisir. Berbeda dengan **Next.js** yang menyederhanakan banyak hal, di Django, kita perlu mengatur semuanya sendiri. Hal ini ini membuat pemahaman tentang alur kerja aplikasi menjadi lebih dalam, mulai dari routing URL, views, models, hingga templates.

3. **Pengalaman Belajar yang Menyeluruh**: Django tidak hanya mempermudah proses pengembangan, tetapi juga membuat kita memahami berbagai hal di balik layar. Kita diharuskan melakukan setup sendiri, seperti konfigurasi database (models), pemetaan URL, hingga logika backend. Dengan demikian, pemahaman kita akan pengembangan aplikasi web menjadi lebih mendalam dan menyeluruh.

Sementara **Next.js** sangat membantu dalam mempercepat proses front-end development dan membuatnya terasa lebih mudah dengan kemudahan _data fetching_ dan pengaturan API, **Django** memberikan kesempatan untuk memahami setiap aspek pengembangan aplikasi dengan lebih mendalam. Ini membantu membangun dasar pengetahuan yang kuat tentang bagaimana sebuah aplikasi bekerja di balik layar.

# Mengapa model pada Django disebut sebagai ORM?

## Apa itu ORM?

**ORM (Object-Relational Mapping)** adalah teknik pemrograman yang memungkinkan pengembang berinteraksi dengan database menggunakan **objek** dalam kode mereka, bukan dengan menulis query SQL secara langsung. Dengan ORM, data yang ada di tabel database diubah menjadi objek yang bisa diolah menggunakan bahasa pemrograman.

## Mengapa Model pada Django Disebut sebagai ORM?

Dalam Django, **model** adalah representasi dari tabel di database. Setiap kelas model yang kita buat di Django secara otomatis dipetakan ke tabel di database, dan Django menangani konversi antara objek Python dan data SQL. Inilah yang membuat Django model disebut sebagai ORM karena:

1. **Objek Python**: Django mengizinkan pengembang untuk berinteraksi dengan database menggunakan objek Python, tanpa harus menulis query SQL.
2. **Mapping Otomatis**: Django secara otomatis memetakan atribut model ke kolom di tabel database. Jadi, jika kita membuat model dengan atribut seperti `name`, `price`, atau `description`, Django akan membuat kolom dengan nama-nama tersebut di tabel database. Dalam kata lain, models adalah sebuah schema untuk database.

# **Tugas 3**

# Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
_Data delivery_ adalah sebuah proses pengiriman data dari satu ke titik ke titik lain. Dalam konteks _web development_, data dikirim dari _client_ ke _server_ dan juga sebaliknya. Alasan mengapa _data delivery_ penting adalah karena _data delivery_ memungkinkan interaksi antara client dan server, yang merupakan inti dari aplikasi web dinamis. Website dinamis penting karena membuat website lebih interactive dan berguna untuk user. Tidak seperti static website yang menampilkan informasi yang sama ke setiap user, website dinamis dapat menampilkan informasi yang dipersonalisasi bergantung siapa yang menggunakan websitenya atau apa yang mereke lakukan

# Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Saya pribadi hanya menggunakan JSON saat membangun aplikasi, contohnya dalam proyek Pokemon Card Generator yang saya buat. Menurut saya, menggunakan JSON terasa lebih intuitif karena penulisan kodenya lebih mudah dipahami. Penulisan JSON seperti menulis struktur data dalam bentuk dictionary atau hashmap. Contohnya, kita bisa langsung mengakses atribut-atribut dengan mudah melalui key, seperti `pokemon["name"]` atau `pokemon["abilities"]`. Sangat sederhana dan mirip seperti struktur data yang kita gunakan dalam banyak bahasa pemrograman. Inilah salah satu alasan mengapa JSON lebih populer dibandingkan XML, terutama dalam pengembangan web.

Namun, dalam XML, kita membutuhkan metode tertentu untuk mengakses atau memanipulasi data. Misalnya, di JavaScript, kita harus menggunakan metode seperti `getElementsByTagName()` atau `getAttribute()` untuk mengambil nilai dari elemen XML. Hal ini membuat proses parsing data lebih rumit dibandingkan JSON, yang bisa langsung diakses dan diproses dengan metode standar.

Contoh pengalaman saya lain adalah ketika saya mencoba membuat anotasi video deadlift untuk proyek computer vision saya. Data anotasi tersebut dalam format XML. Di dalam XML, setiap frame video disimpan dalam elemen <image>, yang menyertakan informasi seperti ID, nama frame, serta data penting lain yang disimpan dalam elemen <points> dan <box>. Misalnya, pada contoh berikut:

```
<image id="0" name="frame_000000" width="608" height="1080">
    <points label="deadlifting" source="manual" points="262.65,563.65;305.53,596.01;..." />
    <box label="deadlifting" source="manual" xtl="211.70" ytl="522.62" xbr="458.80" ybr="943.84" />
</image>
```

Akhirnya, saya menyadari bahwa pemilihan antara JSON dan XML sangat bergantung pada use case. Dalam web development, JSON lebih populer karena lebih ringan, dan mudah dipahami. Sedangkan XML lebih cocok digunakan dalam kasus di mana kita membutuhkan struktur data yang lebih kompleks.

# Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form di Django digunakan untuk memastikan bahwa data yang dikirimkan ke form sesuai dengan aturan validasi yang telah ditetapkan. Aturan validasi ini mencakup beberapa aspek penting,
1. Tipe Data: Django memastikan tipe data yang dimasukkan seperti dengan definisi model yang ada
2. Kelengkapan Field: Django memastikan semuma field yang ditandai sebagai wajib telah diisi oleh user
Hal ini sangat penting untuk menjaga kualitas dan konsistensi pengguna, memastikan data yang dimasukkan ke database dalam format terstruktur. Tentunya hal ini akan memudahkan dalam pengembangan aplikasi.

# Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
