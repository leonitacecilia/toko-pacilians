TUGAS 3 Pemograman Berbasis Platform (PBP)

Nama: Leonita Cecilia
NPM: 2306165710
Kelas: PBP A
Kode Asdos: RZ

Tautan menuju PWS: http://pbp.cs.ui.ac.id/leonita.cecilia/tokopacilians

Jawaban Pertanyaan:
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform? Data delivery diperlukan dalam pengimplementasian sebuah platform untuk memastikan data yang dihasilkan atau dibutuhkan oleh pengguna dan sistem dapat dikirim, diterima, dan diproses dengan benar. Ini memungkinkan platform berfungsi dengan lancar, mendukung interaksi antar pengguna, dan memastikan integritas serta ketersediaan data saat diperlukan untuk analisis, pengambilan keputusan, atau layanan otomatis lainnya. 

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
XML lebih cocok digunakan untuk konfigurasi sistem dan dokumen terstruktur. JSON lebih cocok untuk pertukaran data web, seperti API dan penyimpanan data. Kini, JSON lebih populer dibandingkan XML karena lebih sederhana, lebih mudah dibaca, dan lebih efisien dalam penggunaan storage data. JSON menggunakan struktur yang lebih ringkas (key-value pairs) tanpa tag penutup yang panjang seperti XML, sehingga lebih mudah di-parse dan diproses oleh banyak bahasa pemrograman.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() berfungsi untuk memeriksa apakah data yang dimasukkan ke dalam form telah memenuhi semua validasi yang ditentukan. Method ini mengecek apakah input pengguna sesuai dengan tipe data, panjang, format, atau aturan lainnya yang didefinisikan dalam form. Kita memerlukan method ini untuk memastikan bahwa data yang diproses dan disimpan dalam sistem adalah data yang valid dan sesuai standar, sehingga mencegah error atau data corrupt.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Kita membutuhkan "csrf_token" di Django untuk mencegah serangan Cross-Site Request Forgery (CSRF). Jika tidak menambahkan "csrf_token", penyerang bisa mengeksploitasi pengguna terautentikasi dengan mengirimkan permintaan berbahaya tanpa sepengetahuan mereka. Tanpa token ini, server tidak dapat memverifikasi asal permintaan, sehingga penyerang dapat memanipulasi data atau melakukan tindakan yang tidak sah atas nama pengguna.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
a. Membuat kerangka views dari website
b. Untuk meningkatkan keamanan aplikasi, kita mengubah primary key dari Integer menjadi UUID 
c. Membuat form input data agar user bisa memasukkan data. Data yang diinput user akan ditampilkan pada web HTML.
d. Memprogram agar data bisa dikembalikan dalam bentuk XML dan JSON. 
e. Memprogram agar data berdasarkan ID bisa dikembalikan dalam bentuk XML dan JSON. 
f. Memastikan local server telah berjalan denagan baik, salah satunya dengan melakukan request pada postman.

6. Link Post-Man: https://drive.google.com/drive/folders/18-IZdZOkQc6GAguf3qyYRNWNX3Wd0Ugm?usp=sharing

