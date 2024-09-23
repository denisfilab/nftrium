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
