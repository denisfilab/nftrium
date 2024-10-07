**Nama: Daanish Inayat Rahman**
**NPM: 2306213136**
**Kelas: PBP A**

# Link PWS

**http://daanish-inayat-nftriumm.pbp.cs.ui.ac.id/**

# **Tugas 2**

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

Menurut saya, pemilihan antara JSON dan XML sangat bergantung pada use case. Dalam web development, JSON lebih populer karena lebih ringan, dan mudah dipahami. Sedangkan XML lebih cocok digunakan dalam kasus di mana kita membutuhkan struktur data yang lebih kompleks.

# Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() pada form di Django digunakan untuk memastikan bahwa data yang dikirimkan ke form sesuai dengan aturan validasi yang telah ditetapkan. Aturan validasi ini mencakup beberapa aspek penting,

1. Tipe Data: Django memastikan tipe data yang dimasukkan seperti dengan definisi model yang ada
2. Kelengkapan Field: Django memastikan semuma field yang ditandai sebagai wajib telah diisi oleh user
   Hal ini sangat penting untuk menjaga kualitas dan konsistensi pengguna, memastikan data yang dimasukkan ke database dalam format terstruktur. Tentunya hal ini akan memudahkan dalam pengembangan aplikasi.

# Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

CSRF token adalah nilai unik yang dihasilkan oleh server dan disematkan dalam setiap form di Django untuk melindungi aplikasi dari serangan **Cross-Site Request Forgery (CSRF)**. Kita membutuhkan csrf_token saat membuat form di Django agar memastikan bahwa setiap permintaan yang dikirim berasal dari pengguna yang sah dan bukan dari pihak ketiga yang berbahaya. Jika kita tidak menambahkan csrf_token pada form Django, aplikasi menjadi rentan terhadap serangan CSRF, di mana penyerang dapat memanfaatkan sesi pengguna yang aktif untuk menjalankan tindakan tanpa sepengetahuan atau persetujuan mereka, seperti mengubah data akun, melakukan transaksi finansial, atau mengubah pengaturan penting lainnya.

# Penjelasan Kode

## Pembuatan Page Form

Pertama, saya harus membuat file `forms.py` di directory `main`. Lalu saya membuat Class NFTForm dengan attribut `model = NFT` lalu untuk field, saya memasukkan field yang perlu diisi oleh user seperti `name`, `price`, `description` dst.

Setelah membuat forms.py dan mendefinisikan NFTForm, kita perlu menambahkan fungsi di views.py. File `views.py` dibutuhkan untuk menangani logika aplikasi, seperti menerima data dari form, memvalidasi data, menyimpan data ke database, dan mengembalikan respons yang sesuai kepada pengguna. Tanpa views.py, form yang kita buat tidak akan terhubung ke sistem dan tidak dapat memproses input dari user.
Berikut adalah kode yang ditambahkan ke views.py:

```
def create_nft_entry(request):
    if request.method == "POST":
        form = NFTForm(request.POST, request.FILES)  # Termasuk request.FILES untuk menangani file upload
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = NFTForm()

    context = {'form': form}
    return render(request, "create_nft_entry.html", context)
```

Saya menambahkan fungsi `redirect('main:show_main')` agar ketika berhasil submit suatu form, akan balik ke main untuk melihat hasilnya.

Kemudian, tambahkan path baru di urls.py untuk menghubungkan URL ke fungsi view tersebut:

```
path('create-nft-entry', create_nft_entry, name='create_nft_entry'),
```

Selanjutnya, buat template create_nft_entry.html untuk menampilkan form kepada pengguna. Saya juga menambahkan {% csrf_token %} di dalam form untuk memastikan keamanan form.

## Pembuatan route JSON, dan XML

Selanjutnya, saya menambahkan route untuk menampilkan data NFT dalam format JSON, XML dan juga diakses berdasarkan id (pk). Ini berguna jika kita ingin data NFT dapat diakses oleh aplikasi lain atau digunakan untuk API.
Saya harus membuat fungsi untuk menampilakn data NFT di views.py. Berikut merupakan kodenya

```
from django.http import HttpResponse
from django.core import serializers

def show_xml(request):
    data = NFT.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = NFT.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_token_id(request, token_id):
    data = NFT.objects.filter(token_id=token_id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_token_id(request, token_id):
    data = NFT.objects.filter(token_id=token_id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

Penjelasan Kode
show_xml: Fungsi ini mengambil semua objek NFT dari database dan mengembalikannya dalam format XML.
show_json: Fungsi ini mirip dengan show_xml, tetapi mengembalikan data dalam format JSON.
show_xml_by_token_id: Fungsi ini mengambil objek NFT dengan pk (primary key) tertentu dan mengembalikannya dalam format XML.
show_json_by_token_id: Fungsi ini mengambil objek NFT dengan pk tertentu dan mengembalikannya dalam format JSON.

Setelah menambahkan fungsinya, saya harus menambahakn url baru di urls.py agar route fungsinya dapat dipakai.
Saya menambahkan kode berikut di `urls.py` dalam `main`

```
 path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
path('xml/<str:token_id>/', show_xml_by_token_id, name='show_xml_by_token_id'),
path('json/<str:token_id>/', show_json_by_token_id, name='show_json_by_token_id'),
```

Keempat URL ini dapat diakses melalui postman maupun website biasa.
Contoh:

### `/xml`

![image](https://github.com/user-attachments/assets/dbedc5e1-8ef6-40d2-98d4-f5239caf6833)

### `/json`

![image](https://github.com/user-attachments/assets/dbed5c9e-05a2-46d5-9283-8d211003628b)

### `/json/<token_id>`

![image](https://github.com/user-attachments/assets/e754cfcc-95df-4986-aa0b-0891f91aaa15)

### `/xml/<token_id>`

![image](https://github.com/user-attachments/assets/2ccbe3bb-a527-49c3-a296-5bb8c857e98a)

# **Tugas 4**

## Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`

Kedua fungsi tersebut berfungsi untuk men-direct user ke url baru, tetapi parameter kedua fungsi tersebut berbeda.

Parameter yang dimasukkan fungsi `HttpResponseRedirect()` berupa URL string, nanti fungsi tersebut akan melakukan redirect sesuai parameter yang dimasukkan. Sedangkan parameter yang dimasukkan fungsi `redirect` bisa berbeda - beda. Pertama, di fungsi `redirect` kita bisa memasukkan attribut nama sesuai dengan urlPattern di urls.py

Contoh:

```
path('create-nft-entry', create_nft_entry, name='create_nft_entry'),
```

maka fungsi redirect akan seperti

```
redirect('create_nft_entry')
```

Kedua, Anda juga bisa memasukkan sebuah objek model ke dalam `redirect()`. Django akan menggunakan metode `get_absolute_url()` dari objek tersebut untuk menentukan URL tujuan.

Contoh:

```
def some_view(request):
    nft = NFT.objects.get(id=1)
    return redirect(nft)
```

Dengan syarat, perlu menulis urlpatterns dan metode get_absolute_url di class NFT tersebut. Nantinya, user akan didirect ke url sesuai dengan apa yang tertulis di urlpatterns

## Jelaskan cara kerja penghubungan model NFT dengan User!

Dalam skenario ini, kita ingin menghubungkan model NFT dengan User sehingga setiap NFT yang dibuat oleh pengguna akan terkait dengan pengguna yang membuatnya. Pengguna hanya dapat membuat NFT jika mereka sudah login ke dalam sistem. Proses ini dapat dijelaskan melalui beberapa langkah berikut:

1. Penambahan Field `user` di model NFT
   Pada model NFT, kita menambahkan sebuah field baru yang disebut user. Field ini berfungsi sebagai relasi antara NFT dan pengguna yang membuatnya. Jadi, setiap NFT yang dibuat akan memiliki referensi kepada pengguna yang terautentikasi (user)

2. Pembuatan NFT jika sudah login
   Pengguna hanya dapat membuat NFT setelah mereka login. Hal ini berarti, dalam konteks tugas, halaman pembuatan NFT tidak bisa diakses jika belum login. Dengan cara ini, pembuatan instances dari model (row di table) memastikan field user terisi.

Dengan cara ini, tiap NFT dapat diidentifikasi siapa yang membuat NFTnya karena terdapat reference di field user.

## Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

Django menggunakan kombinasi session dan cookies untuk mengingat pengguna yang telah login. Ketika pengguna login, Django memverifikasi kredensial mereka, seperti username dan password. Jika valid, Django membuat sebuah session di server, yang menyimpan informasi penting terkait pengguna, misalnya user. Selanjutnya, Django menyimpan session ID ke dalam cookie yang dikirimkan ke browser pengguna. Cookie ini berfungsi sebagai pengidentifikasi unik untuk setiap pengguna. Pada permintaan HTTP berikutnya, browser secara otomatis mengirimkan session ID ini kembali ke server, yang memungkinkan Django untuk menghubungkan permintaan tersebut dengan session pengguna yang tersimpan. Dengan cara ini, pengguna tidak perlu login ulang pada setiap interaksi selama session mereka masih aktif.

## Implementasi login, register, logout, dan hubungan model dengan user.

### Implementasi register

Pertama kita perlu import

```
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```

Import UserCreationForm memungkinkan kita untuk menggunakan form yang sudah ada untuk membuat sebuah form register untuk user baru. Lalu buat fungsi register di views.py

```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun Anda telah berhasil dibuat!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)
```

Lalu membuat path baru di urls.py,

```
path('register/', register, name='register'),
```

Tidak lupa membuat template register.html

### Implementasi login

Pertama kita perlu import

```
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
```

Import AuthenticationForm memungkinkan kita untuk menggunakan form yang sudah ada untuk membuat sebuah form login untuk user. Impor authenticate dan login untuk memverifikasi user dan login user. Lalu kita lanjut dengan membuat fungsi login_user di views.py

```
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```

Tidak lupa membuat path baru di urls.py, dan membuat template login.html

### Implementasi logout

Pertama kita perlu import

```
from django.contrib.auth import logout
```

Lalu membuat fungsi logout_user di views.py

```
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Tidak lupa membuat path baru di urls.py,

```
path('logout/', logout_user, name='logout'),
```

Lalu tambahkan tombol logout di main.html dengan cara

```
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
```

## Implementasi hubungan model dengan user

Pertama kita perlu import

```
from django.contrib.auth.models import User
```

Lalu kita perlu menambahkan field user di model NFT.
Tambahkan field tersebut di dalam class NFT.

```
user = models.ForeignKey(User, on_delete=models.CASCADE)
```

Lalu kita perlu mengubah fungsi create_nft_entry di views.py menjadi

```
def create_nft_entry(request):
    if request.method == "POST":
        form = NFTForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            nft = form.save(commit=False)
            nft.user = request.user
            nft.save()
            return redirect('main:show_main')
    else:
        form = NFTForm()
```

Hal ini memastikan setiap NFT yang dibuat oleh user akan dikaitkan dengan user tersebut.

Lalu saya juga perlu memastikan hanya bisa membuat NFT jika sudah login, dengan cara menambahkan

```
@login_required(login_url='/login')
```

di atas fungsi `show_main`. Dengan cara ini, user tidak bisa mengakses halaman utama dan halaman create NFT tanpa login terlebih dahulu sehingga memastikan setiap NFT yang dibuat akan dikaitkan dengan user tersebut.

## Implementasi Cookies dan Last Login Information

Pertama kita perlu import

```
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

Lalu kita perlu menambahkan cookies di fungsi `login_user` di `views.py` agar setiap login, datanya disimpan di cookies dan bisa diakses.

```
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) # Tambahkan ini
            response.set_cookie('last_login', str(datetime.datetime.now())) # Tambahkan ini
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
```

Lalu di `show_main` kita perlu menambahkan cookies ke dalam context agar bisa ditampilkan di template.

```
def show_main(request):
    context = {
        'last_login': request.COOKIES.get('last_login')
    }
    return render(request, 'main.html', context)
```

Nanti di template `main.html` kita bisa menampilkan cookies tersebut dengan cara

```
<h3>Last Login: {{ last_login }}</h3>
```

# **Tugas 5**

## Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas atau Specificity dalam pengambilan CSS selector ditentukan berdasarkan beberapa faktor. Berikut adalah urutan prioritasnya dari yang tertinggi hingga terendah:
1. Inline CSS (misalnya, yang diterapkan langsung pada elemen HTML menggunakan atribut style).
2. ID Selector (menggunakan tanda # diikuti oleh nama ID, misalnya #header).
3. Class Selector, Pseudo-class, dan Attribute Selector (misalnya .container, :hover, atau [type="text"]).
4. Element Selector dan Pseudo-element (misalnya div, h1, atau ::before).
5. Universal Selector (*) dan Inherited Selector (tidak memiliki nilai spesifik).

Jika terdapat beberapa CSS selector untuk suatu elemen HTML, maka CSS selector dengan Specificity yang lebih tinggi akan memiliki prioritas lebih tinggi dan akan diterapkan pada elemen tersebut.

## Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Menurut saya, responsiveness dalam sebuah design website sangat penting karena seorang user yang mengakses website bisa berasal dari berbagai perangkat, seperti desktop, laptop, tablet, atau smartphone. Dengan responsive design, website akan menyesuaikan tampilannya agar tetap terlihat baik dan berfungsi dengan baik di berbagai perangkat tersebut. Hal ini meningkatkan pengalaman pengguna dan memastikan website tetap dapat diakses dengan baik oleh semua pengguna, tanpa peduli perangkat apa yang mereka gunakan. Contohnya website yang belum menerapkan responsive design adalah website siak milik Universitas Indonesia. Pengalaman saya membuka website siak di perangkat hp sangat tidak menyenangkan, tulisa yang terlalu kecil, dan tidak bisa di zoom. Contoh website yang sudah menerapkan responsive design adalah website `apple.com`. Website tersebut menyesuaikan tampilannya dengan baik di berbagai perangkat, mulai dari desktop hingga smartphone.

## Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
1. **Margin** adalah ruang di luar batas elemen yang digunakan untuk memberikan jarak antara elemen satu dengan elemen lainnya di halaman web. Margin tidak memiliki warna atau background, hanya berupa ruang kosong yang memberi jarak.

Kita bisa mengatur margin secara spesifik pada setiap sisi elemen: top (atas), right (kanan), bottom (bawah), dan left (kiri). Untuk mengimplementasikannya, CSS menyediakan beberapa cara dalam mendefinisikan margin:
```css
/* Margin pada setiap sisi elemen */
margin-top: 10px;    /* Margin atas */
margin-right: 20px;  /* Margin kanan */
margin-bottom: 30px; /* Margin bawah */
margin-left: 40px;   /* Margin kiri */
```

2. **Border**: Border adalah garis yang mengelilingi elemen. Border digunakan untuk memberikan garis pembatas pada elemen. Border memiliki ketebalan, warna, dan jenis (solid, dashed, dotted, double, dll.). Untuk mengimplementasikan border, kita bisa menggunakan properti CSS `border` dengan nilai ketebalan, warna, dan jenis.
```css
/* Border pada setiap sisi elemen */
border: 1px solid black; /* Border dengan ketebalan 1px, jenis solid, dan warna hitam */

/* Border spesifik pada setiap sisi elemen */
border-top: 2px dashed red;    /* Border atas dengan ketebalan 2px, jenis dashed, dan warna merah */
border-right: 3px dotted blue; /* Border kanan dengan ketebalan 3px, jenis dotted, dan warna biru */
border-bottom: 4px double green; /* Border bawah dengan ketebalan 4px, jenis double, dan warna hijau */
border-left: 5px solid purple; /* Border kiri dengan ketebalan 5px, jenis solid, dan warna ungu */
```

3. **Padding**: Padding adalah ruang di dalam batas elemen dan border. Padding digunakan untuk memberikan jarak antara konten elemen dengan border. Padding tidak memiliki warna atau background, hanya berupa ruang kosong. Untuk mengimplementasikan padding, kita bisa menggunakan properti CSS `padding` dengan nilai dalam satuan px, em, atau %.
```css
/* Padding pada setiap sisi elemen */
padding: 10px 20px 30px 40px; /* Padding atas 10px, kanan 20px, bawah 30px, kiri 40px */

/* Padding spesifik pada setiap sisi elemen */
padding-top: 10px;    /* Padding atas */
padding-right: 20px;  /* Padding kanan */
padding-bottom: 30px; /* Padding bawah */
padding-left: 40px;   /* Padding kiri */
```

Berikut merupakan ilustrasi dari border, padding dan margin.
![alt text](https://www.avajava.com/tutorials/cascading-style-sheets/how-are-margins-borders-padding-and-content-related/how-are-margins-borders-padding-and-content-related-01.gif)

## Jelaskan konsep flex box dan grid layout beserta kegunaannya!
1. Flexbox (Flexible Box Layout)
Flexbox adalah modul CSS yang dirancang untuk menyusun elemen dalam satu dimensi—baik dalam baris (horizontal) maupun kolom (vertikal). Flexbox memungkinkan distribusi ruang di antara elemen dan kemampuan untuk mengatur ukuran serta posisi elemen secara fleksibel, sehingga sangat ideal untuk tata letak responsif.
Jadi, di flexbox terdapat yang namanya main axis dan cross axis. Main axis adalah arah utama dari flex container, sedangkan cross axis adalah arah yang tegak lurus terhadap main axis. Hal ini bisa dilihat dari styling flex-direction. Jika flex-direction: row, maka main axis adalah horizontal, sedangkan jika flex-direction: column, maka main axis adalah vertical. 

Kegunaan Flexbox:
- Menyusun elemen dalam satu baris atau kolom.
- Mengatur perataan (alignment) elemen secara vertikal atau horizontal.
- Mengontrol distribusi ruang antar elemen, termasuk fleksibilitas ukuran elemen.
- Mengelola urutan elemen tanpa mengubah urutan HTML.

Contoh Penggunaan Flexbox:
a. Menyusun Elemen dalam Satu Baris dengan Center Alignment
```html
<div class="flex-container">
  <div class="flex-item">Item 1</div>
  <div class="flex-item">Item 2</div>
  <div class="flex-item">Item 3</div>
</div>
```
```css
.flex-container {
  display: flex;
  justify-content: center; /* Mengatur perataan horizontal */
  align-items: center;    /* Mengatur perataan vertikal */
  height: 200px;
  background-color: #f0f0f0;
}

.flex-item {
  background-color: #4CAF50;
  color: white;
  padding: 20px;
  margin: 10px;
  text-align: center;
}
```

2. Grid Layout
Grid Layout adalah modul CSS yang memungkinkan pembuatan tata letak dua dimensi—baik dalam baris maupun kolom. Grid Layout sangat cocok untuk membuat layout yang lebih kompleks, seperti dashboard, layout majalah, atau galeri foto, di mana kontrol atas kedua dimensi diperlukan.
Kegunaan Grid Layout:
- Membuat layout dua dimensi (baris dan kolom) secara simultan.
- Mengatur ukuran dan posisi elemen dengan presisi.
- Membuat grid responsif yang dapat beradaptasi dengan berbagai ukuran layar.
- Memudahkan pembuatan layout kompleks tanpa harus menggunakan banyak elemen nested.

Contoh Penggunaan Grid Layout:
a. Membuat Grid Container dan Menyusun Elemen dalam Grid dengan 3x3
```html
<div class="grid-container">
  <div class="grid-item">1</div>
  <div class="grid-item">2</div>
  <div class="grid-item">3</div>
  <div class="grid-item">4</div>
  <div class="grid-item">5</div>
  <div class="grid-item">6</div>
  <div class="grid-item">7</div>
  <div class="grid-item">8</div>
  <div class="grid-item">9</div>
</div>
```
```css
.grid-container {
  display: grid;
  grid-template-columns: auto auto auto;
  background-color: #2196F3;
  padding: 10px;
}
.grid-item {
  background-color: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(0, 0, 0, 0.8);
  padding: 20px;
  font-size: 30px;
  text-align: center;
}
```
Nanti tampilannya akan seperti ini
Image

## Implementasi UI Login, Register, Navbar, dan NFT

### Implementasi UI Login dan Register
Untuk parent containernya, memiliki style
```html
<div class="flex items-center justify-center min-h-screen bg-[#00040F]">
```
Lalu terdapat container untuk form login dan register
```html
<div class="w-full max-w-md bg-gray-800 rounded-lg shadow-md p-8">
```
Dengan cara parent container memiliki style seperti flex, items-center, dan justify-center, maka form login dan register akan berada di tengah layar.
Lalu tinggal implementasi theme color dan style untuk field input, button, dan lainnya.


### Implementasi Navbar
Navbar memiliki konsep dan styling seperti berikut
```html
    <nav class="bg-gray-900 shadow-md">	
    	<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
			<div class="flex justify-between h-16">
                <links>
                </links>
                <auth>
            </div>
        </div>
    </nav>
```
Parent container dari navbar memiliki style seperti bg-gray-900 dan shadow-md. Parent container ini akan memiliki width screen dan height dari childnya. Lalu terdapat child container dengan style `max-w-7xl`, hal ini membuat sebuah container yang dengan panjang lebih kecil dari parent containernya dan berada di tengah parent container karena ada styling `mx-auto`. Lalu terdapat flex justify-between, hal ini membuat child container di dalamnya akan berada di sisi kiri dan kanan. Dalam konteks ini, justify-between akan membuat link berada di sisi kiri dan auth di sisi kanan.

Untuk implementasi navbar, terdapat dua versi: desktop dan mobile. 
- **Navbar Desktop**: Disembunyikan di mobile. Muncul jika lebar layar >= 640px.
- **Navbar Mobile**: Disembunyikan di desktop. Muncul jika lebar layar < 640px.

Styling `hidden` digunakan untuk menyembunyikan elemen yang tidak sesuai dengan width screen.

Perbedaan utamanya adalah penggunaan flex-col dan flex-row.

- Desktop: Links dan auth menggunakan flex-row, artinya elemen disusun secara horizontal.
- Mobile: Links dan auth menggunakan flex-col, artinya elemen disusun secara vertikal. Menu akan muncul jika tombol hamburger diklik, yang diatur dengan JavaScript.
```javascript
function toggleMobileMenu() {
    const menu = document.getElementById("mobile-menu");
    const buttons = document.querySelectorAll('nav button[type="button"] svg');

    if (menu.classList.contains("hidden")) {
        menu.classList.remove("hidden");
        // Tampilkan ikon close
        buttons[0].classList.add("hidden");
        buttons[1].classList.remove("hidden");
    } else {
        menu.classList.add("hidden");
        // Tampilkan ikon hamburger
        buttons[0].classList.remove("hidden");
        buttons[1].classList.add("hidden");
    }
}
```
Function di atas akan menampilkan menu mobile jika tombol hamburger diklik, dan menyembunyikan menu mobile jika tombol close diklik dengan cara menambahkan style hidden dan remove style hidden.


### Implementasi NFT
Untuk implementasi NFT, kita bisa menggunakan grid layout untuk menampilkan NFT dalam grid. Berikut adalah kodenya, saya menggunakan breakpoint dari tailwindcss untuk membuat grid responsive. Bergantung terhadap ukuran layar, jumlah kolom dalam grid akan berubah.
```html
<div class="container mx-auto px-4">
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 auto-cols-auto">
        {% for nft in nfts %}
            {% include 'components/nftcard.html' with nft=nft %}
        {% empty %}
        <p class="text-center text-gray-50  0 col-span-full">
            No NFTs available at the moment.
        </p>
        {% endfor %}
    </div>
</div>
```
Saya juga menambahkan lift-off effect ketika suatu nft di hover. Berikut adalah kodenya
```html
{% load static %}
<div
  class="max-w-md rounded-lg overflow-hidden shadow-lg transform transition-transform hover:-translate-y-2 flex flex-col ease-in-out duration-300 h-fit"
  style="box-shadow: 0 8px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);"
  onmouseover="this.style.boxShadow='0 0 20px 0 rgba(255, 255, 255, 0.5), 0 6px 10px -2px rgba(255, 255, 255, 0.5)';"
  onmouseout="this.style.boxShadow='0 8px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)';"
>
```
Ketika suatu nft di hover, maka akan terjadi perubahan style box-shadow.

Untuk implementasi edit dan delete, saya menambahkan container di bawah nftcard yang berisi tombol edit dan delete. Ketika tombol edit diklik, maka akan diarahkan ke halaman edit nft. Ketika tombol delete diklik, maka akan muncul modal konfirmasi delete.

# **Tugas 6**

## Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Javascript berguna dalam pengembangan aplikasi web karena memungkinkan kita untuk membuat website yang lebih interaktif dan dinamis. Misalnya, kita bisa membuat elemen muncul atau hilang, mengubah warna elemen, menampilkan pesan popup, atau mengirim data ke server tanpa perlu me-refresh halaman berdasarkan user activity atau event listener. Tidak hanya itu, dengan Javascript kita bisa membuat website yang lebih responsif dan user-friendly, seperti validasi form, autocomplete, infinite scroll, dan lainnya. Dengan kata lain, Javascript memungkinkan kita untuk membuat website yang lebih menarik, interaktif, dan user-friendly.


## Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
`await` digunakan untuk menunggu hasil dari suatu operasi asynchronous, seperti fetch() yang mengambil data dari server. Ketika kita menggunakan fetch() tanpa await, maka fetch() akan mengembalikan Promise yang belum selesai. Dengan menggunakan await, kita menunggu fetch() selesai dan mengembalikan data yang diambil dari server. Jika kita tidak menggunakan await, maka kode selanjutnya akan dieksekusi sebelum fetch() selesai, yang berpotensi menyebabkan error atau data yang tidak lengkap.

## Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Django menggunakan mekanisme CSRF (Cross-Site Request Forgery) untuk melindungi website dari serangan CSRF. Saat menggunakan AJAX, kita perlu menonaktifkan CSRF protection untuk view yang digunakan untuk AJAX POST karena browser akan memblokir request POST yang tidak memiliki CSRF token. Dengan menggunakan decorator `@csrf_exempt`, kita memberitahu Django untuk tidak memeriksa CSRF token pada view tersebut sehingga request POST dari AJAX akan berhasil dilakukan tanpa error. Namun, perlu diingat bahwa AJAX bukanlah pengecualian dari aturan CSRF protection sehingga perlu hati-hati dalam menggunakan `@csrf_exempt`. Menggunakan @csrf_exempt pada view yang menangani **AJAX POST bukanlah solusi yang ideal** karena hal ini akan mematikan proteksi CSRF secara keseluruhan pada view tersebut

## Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Hal ini karena frontend berjalan di perangkat pengguna yang dapat dengan mudah dimanipulasi, seperti melalui alat developer browser atau alat eksternal yang memungkinkan pengguna mengubah atau mengabaikan validasi yang ada. Pengguna bahkan bisa melewati seluruh frontend dan mengirimkan data langsung ke backend tanpa melalui validasi, sehingga pembersihan di frontend saja tidak cukup untuk menjamin keamanan dan integritas data yang masuk ke server.

Di sisi lain, backend adalah lapisan terakhir yang dapat dipercaya dan berada di bawah kendali penuh pengembang. Pembersihan di backend memastikan bahwa data yang masuk telah sesuai dengan aturan dan standar yang telah ditetapkan oleh sistem, serta melindungi dari serangan seperti Cross-Site Scripting (XSS) atau SQL Injection. Dengan melakukan pembersihan di backend, aplikasi dapat memproses data dengan aman dan konsisten, terlepas dari bagaimana atau dari mana data tersebut dikirim. Backend memastikan keamanan dan keandalan sistem dengan menjaga data yang diproses telah dibersihkan secara menyeluruh sebelum digunakan dalam sistem.

## Implementasi AJAX dan Modal saat add NFT

### Implementasi Modal
Pertama, kita perlu menambahkan modal di dalam template `main.html`. Modal ini akan muncul ketika tombol "Add NFT" diklik. Berikut adalah snippet kode modal yang ditambahkan di dalam template `main.html`:

```html
	<div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
```
Konsepnya adalah modal akan muncul ketika tombol "Add NFT" diklik, nanti style hidden akan dihilangkan menggunakana javascript sehingga modal akan muncul.
Caranya dengan menambahkan event listener pada tombol "Add NFT" yang akan mengubah style modal menjadi visible ketika tombol diklik.

```javascript
    function showModal() {
		const modal = document.getElementById('crudModal');
		const modalContent = document.getElementById('crudModalContent');

		modal.classList.remove('hidden'); 
		setTimeout(() => {
			modalContent.classList.remove('opacity-0', 'scale-95');
			modalContent.classList.add('opacity-100', 'scale-100');
		}, 50); 
	}
``` 

Nanti di buttonnya akan ditambahkan attribut `onclick="showModal()"`. Tidak hanya itu, ketika user memilih untuk keluar modal dengan cara klik button close, maka akan dihilangkan style visible dan modal akan hilang.
```javascript
    function hideModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modalContent.classList.remove('opacity-100', 'scale-100');
        modalContent.classList.add('opacity-0', 'scale-95');
        setTimeout(() => {
            modal.classList.add('hidden');
        }, 300); 
    }
```

### Implementasi AJAX
Sederhananya, ketika user menambahkan suatu NFT, data yang dimasukkan dalam form field akan dikirim ke database Django. Kemudian, terdapat fungsi yang bertugas untuk mengambil data dari database dengan output JSON melalui routing `api/json`. Fungsi ini akan dipanggil setiap kali pengguna menambahkan NFT. Data yang didapat dari hasil pengambilan ini akan diproses menjadi komponen HTML dan ditambahkan dengan memodifikasi bagian grid items pada DOM.

Hal ini bisa dicapai dengan menambahkan event listener pada form submit. Ketika form di submit, maka akan diambil data dari form field dan dikirim ke server menggunakan fetch(). Setelah mendapat respon dari server, data yang diterima akan diproses dan dibuat menjadi komponen HTML yang akan ditambahkan ke dalam container grid. Untuk menambahkan komponen HTML, kita bisa menggunakan innerHTML seperti yang tertulis di fungsi `refreshNFTEntries()`.

Fungsi untuk submit data ke database
```javascript
    function addNFTEntry() {
		fetch("{% url 'main:add_nft_entry_ajax' %}", {
		method: "POST",
		body: new FormData(document.querySelector('#nftEntryForm')),
		})
		.then(response => refreshNFTEntries())

		document.getElementById("nftEntryForm").reset(); 
		document.querySelector("[data-modal-toggle='crudModal']").click();

		return false;
	}
```

Fungsi untuk fetching data NFT setiap tambah NFT atau load page pertama kali
```javascript
    async function getNFTEntry() {
        console.log("Fetching NFT entries...");
        try {
            const response = await fetch("{% url 'main:show_json' %}");
            console.log("Response received:", response);
            const data = await response.json();
            console.log("JSON data:", data);
            return data;
        } catch (error) {
            console.error("Error fetching NFT entries:", error);
        }
    }

    function refreshNFTEntries() {
        document.getElementById("nft_entry_grid").innerHTML = "";
        let nftEntries = ""
        getNFTEntry().then((data) => {
            data.forEach((nft) => {
                const nftEntries = `
                    <div
                        class="max-w-md rounded-lg overflow-hidden shadow-lg transform transition-transform hover:-translate-y-2 flex flex-col ease-in-out duration-300 h-fit"
                        style="box-shadow: 0 8px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);"
                        onmouseover="this.style.boxShadow='0 0 20px 0 rgba(255, 255, 255, 0.5), 0 6px 10px -2px rgba(255, 255, 255, 0.5)';"
                        onmouseout="this.style.boxShadow='0 8px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)';"
                    >
                        <div class="relative w-full">
                            <img
                                class="w-full h-auto object-cover"
                                src="media/${nft.fields.image}"
                                alt="${DOMPurify.sanitize(nft.fields.name)}"
                            />

                            <div
                                class="absolute inset-0 bg-black bg-opacity-50 opacity-0 hover:opacity-100 transition-opacity duration-300 flex flex-col justify-end items-start text-white text-center p-4 pb-16"
                            >
                                <h2 class="text-2xl font-bold">${DOMPurify.sanitize(nft.fields.name)}</h2>
                                <p class="text-lg">${DOMPurify.sanitize(nft.fields.price)} ETH</p>
                                <p class="text-sm">Created by: ${DOMPurify.sanitize(nft.fields.creator)}</p>
                            </div>
                            
                            <div
                                class="bottom-0 w-full flex justify-between px-4 py-2 rounded-b-lg"
                                style="background: linear-gradient(
                                    -168.39deg,
                                    #ffffff -278.56%,
                                    #6d6d6d -78.47%,
                                    #11101d 91.61%
                                );"
                            >
                                <a
                                    href="edit-nft/${nft.pk}/"
                                    class="bg-gray-800 hover:bg-gray-700 text-white py-1 px-3 rounded z-10"
                                >
                                    Edit
                                </a>
                                
                                <button
                                    class="border-red-700 border-[3px] text-red-700 hover:bg-red-700 hover:text-white py-1 px-3 rounded z-10"
                                    onclick="openModal('modal-delete-${DOMPurify.sanitize(nft.fields.id)}')"
                                >
                                    Delete
                                </button>
                            </div>
                        </div>

                        <div
                            id="modal-delete-${DOMPurify.sanitize(nft.fields.id)}"
                            class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 hidden rounded-lg"
                        >
                            <div class="bg-gray-800 rounded-lg shadow-lg w-11/12 md:max-w-md">
                                <div class="px-6 py-4">
                                    <h2 class="text-xl font-bold mb-4 text-white">Confirm Delete</h2>
                                    <p class="text-gray-300">
                                        Are you sure you want to delete NFT
                                        <strong>${DOMPurify.sanitize(nft.fields.name)}</strong>?
                                    </p>
                                </div>
                                <div class="px-6 py-4 flex justify-end space-x-4">
                                    <button
                                        class="bg-gray-800 hover:bg-gray-700 text-white py-1 px-3 rounded z-10"
                                        onclick="closeModal('modal-delete-${DOMPurify.sanitize(nft.fields.id)}')"
                                    >
                                        Cancel
                                    </button>
                    
                                        <a
                                            class="border-red-700 border-[3px] text-red-700 hover:bg-red-700 hover:text-white py-1 px-3 rounded z-10"
                                            href="/delete-nft/${nft.pk}"
                                        >
                                            Delete
                                        </a>
                                </div>
                            </div>
                        </div>
                    </div>
                `;
                document.getElementById("nft_entry_grid").innerHTML += nftEntries;});
        });
    }

```


