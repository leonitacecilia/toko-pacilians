TUGAS 2 PBP

Nama: Leonita Cecilia
NPM: 2306165710
Kelas: PBP A
Kode Asdos: RZ

Tautan menuju PWS: http://pbp.cs.ui.ac.id/leonita.cecilia/tokopacilians

Jawaban Pertanyaan:
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

(a). Pertama-tama, saya membuat sebuah repositori baru di github, yang dapat diakses di link https://github.com/leonitacecilia/toko-pacilians.git
(b). Kemudian, saya membuat direktori dan mengaktifkan virtual environment untuk menginisiasi projek Django. Saya memastikan projek telah berhasil dijalankan pada local host.
(c). Langkah berikutnya, saya membuat aplikasi baru dengan nama 'main' dan membuat template website. 
(d). Selanjutnya, saya mengisiniasi atribut nama, kelas, produk, harga, nutrisi, dan tingkat kemanisan buah.
(e). Kemudian, saya melakukan migrasi model. 
(f). Langkah terakhir, saya menghubungkan view dengan template lalu mengonfigurasi routing URL hingga akhirnya tampilan website telah dapat dilihat. Tak lupa, saya melakukan push ke github serta pws untuk submisi tugas.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
Request client -> Internet -> Python, Django -> views.py -> models.py -> view.py -> berkas html -> Python, Django -> Internet -> Web Page

Gambar bagan dapat dilihat pada link: https://drive.google.com/file/d/1C4YwC4r42SJI0EHbChB0JV2lpOWTdvH1/view?usp=sharing (Sumber: slide PBP Scele)

Penjelasan bagan: 
(a). Client memberikan request ke internet dengan cara mengclick sebuah URL.
(b). Internet akan meneruskan request ke web aplikasi berbasis Django (dalam kasus ini: Python). 
(c). Python akan mengambil argument dari request sebelumnya dan mengekstraknya ke views.py (kode python).
(d). Python akan mengakses models.py dan mengambil database jika diperlukan. Setelah itu, data akan ditransfer ke views.py.
(e). views.py mengirimkan kode ke template html yang telah tersedia.
(f). Template html akan dimerged dan diproses valuenya dengan menjalankan manage.py.  
(g). Hasil dari dijalankannya manage.py akan dikirimkan kembali ke python yang berbasis Django.
(h). Kemudian, hasil akan diteruskan ke internet dan ditampilkan melalui web page.
(i). Akhirnya, client dapat melihat tampilan page melalui web page, sesuai dengan request URL yang diketikkan di awal. 

3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git berfungsi untuk manajemen kode, yang berperan sebagai sistem kontrol dalam pengembangan perangkat lunak. Git mampu melacak perubahan pada kode sumber dan bersifat terdistribusi sehingga memungkinkan para developer untuk berkolaborasi dan bekerja secara bersama-sama. Git juga mendukung adanya percabangan, yang memungkinkan untuk melakukan pengembangan perangkat lunak secara non-paralel.  

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django memiliki banyak keunggulan, di antaranya:
a. Bersifat open source, yakni kode dapat dogunakan, dimodifikasi, dan diakses oleh siapapun. 
b. Sistem yang mampu berjalan dengan cepat.
c. Memiliki fitur bawaan yang lengkap, seperti autentikasi, ORM, admin panel, dan sistem routing yang mampu memudahkan para developer. 
d. Memiliki tingkat keamanan yang tinggi.
e. Mampu bekerja pada skala besar, dengan kinerja tetap optimal.
f. Fleksibel dan dapat digunakan pada berbagai macam proyek, mulai dari proyek sederhana hingga proyek yang kompleks.

5. Mengapa model pada Django disebut sebagai ORM?
Model pada Django memungkinkan adanya interaksi dengan database sehingga membuat setiap objek yang ada pada Python dapat langsung terhubung dengan basis data, tanpa harus menuliskan kode SQL apapun.

