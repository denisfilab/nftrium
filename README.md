# Link PWS

**google.com**

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

# Mengapa Django Cocok sebagai Permulaan Pembelajaran Pengembangan Perangkat Lunak?

Saya sudah pernah menggunakan **Next.js**, framework yang cukup bagus, terutama untuk pengembangan front-end. Namun, ada beberapa alasan mengapa **Django** mungkin lebih baik untuk permulaan pembelajaran pengembangan perangkat lunak:

1. **Full-Stack Framework**: Django adalah framework full-stack, artinya Django menangani semua aspek pengembangan aplikasi, dari front-end hingga back-end, termasuk database sehingga pemula dapat belajar seluruh proses pengembangan aplikasi web dalam satu framework.

2. **Struktur yang Terorganisir**: Django memiliki struktur yang sangat terorganisir dan terstandarisasi. Hal ini memudahkan pemula untuk memahami alur kerja aplikasi, mulai dari URL routing, views, models, hingga templates.

3. **Konsep MVC (Model-View-Controller)**: Django menggunakan arsitektur **MVC**, MVC sangat baik untuk pemahaman dasar tentang pemisahan antara logika bisnis dan presentasi. Hal ini mengajarkan konsep pemrograman yang lebih rapi dan terstruktur.

Meskipun **Next.js** juga sangat kuat, terutama untuk **front-end** dan aplikasi berbasis React, Django memberikan pengalaman belajar yang lebih menyeluruh bagi pemula yang ingin memahami **pengembangan aplikasi web** dari ujung ke ujung.

# Mengapa model pada Django disebut sebagai ORM?

## Apa itu ORM?

**ORM (Object-Relational Mapping)** adalah teknik pemrograman yang memungkinkan pengembang berinteraksi dengan database menggunakan **objek** dalam kode mereka, bukan dengan menulis query SQL secara langsung. Dengan ORM, data yang ada di tabel database diubah menjadi objek yang bisa diolah menggunakan bahasa pemrograman.

## Mengapa Model pada Django Disebut sebagai ORM?

Dalam Django, **model** adalah representasi dari tabel di database. Setiap kelas model yang kita buat di Django secara otomatis dipetakan ke tabel di database, dan Django menangani konversi antara objek Python dan data SQL. Inilah yang membuat Django model disebut sebagai ORM karena:

1. **Objek Python**: Django mengizinkan pengembang untuk berinteraksi dengan database menggunakan objek Python, tanpa harus menulis query SQL.
2. **Mapping Otomatis**: Django secara otomatis memetakan atribut model ke kolom di tabel database. Jadi, jika kita membuat model dengan atribut seperti `name`, `price`, atau `description`, Django akan membuat kolom dengan nama-nama tersebut di tabel database. Dalam kata lain, models adalah sebuah schema untuk database.
