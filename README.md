TUGAS 6 Pemograman Berbasis Platform (PBP)

Nama: Leonita Cecilia
NPM: 2306165710
Kelas: PBP A
Kode Asdos: RZ

Tautan menuju PWS: http://pbp.cs.ui.ac.id/leonita.cecilia/tokopacilians

Jawaban Pertanyaan:
1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
Penggunaan JavaScript dalam pengembangan aplikasi web bermanfaat untuk membuat halaman web menjadi dinamis dan interaktif sehingga meningkatkan pengalaman pengguna. JavaScript memungkinkan perubahan konten secara langsung tanpa harus memuat ulang halaman, seperti menampilkan informasi berdasarkan waktu dan melakukan validasi form. Selain itu, JavaScript dapat digunakan untuk mengubah elemen visual secara real-time (seperti CSS). JavaScript juga membantu meringankan beban server karena sebagian besar eksekusi dilakukan di browser pengguna.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
Penggunaan await saat menggunakan fetch() memungkinkan kita untuk menunggu hingga promise yang dihasilkan oleh fetch() teratasi sebelum melanjutkan eksekusi kode. Hal ini berarti kita dapat langsung bekerja dengan data yang diambil tanpa perlu menggunakan .then(). Jika kita tidak menggunakan await, kode akan terus dieksekusi tanpa menunggu respons dari fetch(), yang dapat mengakibatkan error atau nilai undefined saat mencoba mengakses data yang belum tersedia.
 
3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Penggunaan decorator "csrf_exempt" pada view yang digunakan untuk AJAX POST diperlukan karena AJAX requests sering kali tidak menyertakan CSRF token, yang dapat menyebabkan error 403 Forbidden jika tidak ada token yang valid. Dengan menambahkan "@csrf_exempt", pengecekan token CSRF untuk permintaan tersebut diabaikan, memungkinkan permintaan POST diproses tanpa memerlukan token. Hal ini memudahkan integrasi AJAX dalam aplikasi web dan memastikan bahwa permintaan dapat diproses meskipun token CSRF tidak disertakan.
 
4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Pembersihan data di backend tetap diperlukan meskipun kita menggunakan library JavaScript seperti DOMPurify di frontend karena DOMPurify hanya membersihkan data yang akan ditampilkan dalam format HTML di aplikasi kita. Jika aplikasi kita menyediakan API dalam format lain seperti JSON atau XML, data yang dikirim melalui API tersebut tidak akan dibersihkan oleh DOMPurify, sehingga data yang "kotor" masih bisa diakses. Oleh karena itu, pembersihan di backend diperlukan untuk memastikan semua data yang disimpan dan diproses, baik melalui HTML maupun API, selalu aman dan bersih dari potensi serangan atau input berbahaya.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
a. Menambahkan pesan error saat pengguna gagal login.
b. Mengimplementasikan fungsi untuk menambahkan mood menggunakan AJAX serta mengatur routing untuk mendukung fungsi AJAX tersebut.
c. Menambahkan data entry produk ke dalam aplikasi menggunakan fetch() API secara asinkronus.
d. Mengintegrasikan fungsi refreshProductEntries untuk memperbarui data produk secara otomatis tanpa harus memuat ulang halaman.
e. Membuat modal sebagai form untuk memfasilitasi penambahan mood dengan tampilan yang lebih interaktif.
f. Menggunakan AJAX untuk menambahkan data produk ke dalam aplikasi secara dinamis dan cepat.
g. Melindungi aplikasi dari serangan XSS dengan menambahkan fitur sanitasi input melalui penggunaan fungsi strip_tags.
h. Membersihkan data yang diambil dari input pengguna dengan menggunakan DOMPurify untuk mencegah penyalahgunaan kode berbahaya.