TUGAS 5 Pemograman Berbasis Platform (PBP)

Nama: Leonita Cecilia
NPM: 2306165710
Kelas: PBP A
Kode Asdos: RZ

Tautan menuju PWS: http://pbp.cs.ui.ac.id/leonita.cecilia/tokopacilians

Jawaban Pertanyaan:
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Urutan prioritas pengambilan CSS selector dari yang paling tinggi hingga paling rendah adalah:
(1) Inline style, yakni style yang didefinisikan di dalam style tag. contoh: "<h1 class="class1" style="color: red;" id="title1">HTML5 Example Page</h1>" akan menampilkan warna merah.
(2) ID Selector. Hal ini dikarenakan ID selector bersifat unik, lebih spesifik dibandingkan kelas atau elemen. ID Selector biasanya ditandai dengan simbol tagar #.
(3) Class Selector, diterapkan berdasarkan kelas. Umumnya ditandai dengan awalan simbol titik.
(4) Tag selector, merupakan style pada HTML yang bersifat umum dan tidak spesifik, seperti p, h1, div.
 
3. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design penting dalam pengembangan aplikasi web karena user mengakses web dari berbagai perangkat, seperti handphone, ipad, atau komputer dengan ukuran layar yang berbeda. Tanpa responsive design, tampilan sebuah website bisa menjadi berantakan di layar kecil atau besar, membuat pengguna sulit untuk membaca konten atau menggunakan fitur yang ada. Contoh aplikasi yang telah menerapkan responsive design: Linkedin. Contoh aplikasi yang belum menerapkan responsive design: GoJek (apabila dibuka di tablet, layout tetap memakai template handphone).

4. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin adalah area kosong di sekitar border (transparan)
- Border adalah garis tepian yang mengelilingi konten dan paddingnya
- Padding adalah area kosong di sekitar konten (transparan)
Salah satu cara untuk mengimplementasikannya dapat dilihat pada code berikut ini:
.element {
  margin: 20px;  /* Jarak elemen dari elemen lainnya */
  border: 2px solid black;  /* Border dengan ketebalan 2px dan warna hitam */
  padding: 15px;  /* Jarak antara konten elemen dan bordernya */
}
 
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox (Flexible Box Layout) adalah cara untuk mengatur tata letak elemen di web yang memberikan kemudahan untuk mengatur dan merapikan elemen dalam satu baris atau kolom. Dengan Flexbox, kita dapat menyusun elemen secara horizontal atau vertikal dengan mudah serta mengatur ruang di antara elemen secara otomatis. Sebagai contoh, kita dapat mengatur elemen-elemen agar rata di tengah, ke kiri, atau ke kanan.

Sementara itu, Grid Layout adalah metode yang memungkinkan untuk membuat desain yang lebih kompleks dengan menggunakan baris dan kolom. Grid cocok untuk mengatur elemen dalam format yang lebih terstruktur sehingga  bisa menciptakan tata letak yang rumit dan sesuai dengan keinginan. Dengan Grid, kita bisa menentukan ukuran dan posisi elemen dengan lebih tepat, cocok untuk penggunaan responsif. 
 
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
(1) Menambahkan Bootstrap ke aplikasi
(2) Menambahkan fitur edit product dan memunculkannya pada button dengan cara membuat fungsi baru di views.py, ditambahkan ke urls.py, dan menambahkan button pada main.html
(3) Menambahkan fitur hapus product dan memunculkannya pada button dengan cara membuat fungsi baru di views.py, ditambahkan ke urls.py, dan menambahkan button pada main.html
(4) Menambahkan navbar pada aplikasi
(5) Mengonfigurasi static file pada aplikasi
(6) Menambahkan styles pada aplikasi dengan cara memodifikasi base.html terlebih dahulu untuk menambahkan script Tailwind kemudian menambahkan custom style di global.css
