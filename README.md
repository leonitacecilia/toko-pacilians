TUGAS 4 Pemograman Berbasis Platform (PBP)

Nama: Leonita Cecilia
NPM: 2306165710
Kelas: PBP A
Kode Asdos: RZ

Tautan menuju PWS: http://pbp.cs.ui.ac.id/leonita.cecilia/tokopacilians

Jawaban Pertanyaan:
1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
Fungsi HttpResponseRedirect() mengarahkan user ke URL yang dimasukkan dalam tanda kurung dan hanya dapat diisi oleh URL, sedangkan fungsi Redirect() mampu mengarahkan user ke berbagai jenis input (tidak hanya terbatas pada URL), seperti view names dan object.
 
2. Jelaskan cara kerja penghubungan model Product dengan User!
User didefinisikan sebagai class dan Product didefinisikan sebagai atribut yang dimiliki user. Hal ini memiliki makna men-assign nilai Foreign Key ke setiap User dan setiap User bisa memiliki atribut Product yang berbeda-beda.

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication adalah proses memverifikasi identitas user yang hendak login, sedangkan authorization adalah proses memberikan role tertentu kepada user untuk memberikan batasan akses terhadap suatu website. Saat pengguna login, pengguna melakukan authentication. Apabila valid, Django akan memproses data dari pengguna yang login untuk men-assignnya ke role tertentu secara spesifik, seperti Admin, Guest, atau role lainnya. Hal ini turut menjadi batasan terkait sejauh apa akses website yang dimiliki oleh user yang login. 
 
4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django dapat mengingat pengguna yang telah login dengan menggunakan cookie. Cookie memiliki session ID yang dapat dianggap sebagai token untuk menyimpan session yang unik pada aplikasi web tertentu. Session ID kemudian dipetakan ke suatu struktur data pada sisi web server. Cookie sendiri terbagi menjadi 2, yakni session cookie yang bersifat lebih temporary dan persistent cookie yang mampu menyimpan data dalam durasi yang lebih lama. Kegunaan lain dari cookie meliputi: (1) user tracking, yakni bisa melacak aktivitas user; (2) pelacakan preferensi user, yakni kecenderungan hal yang disukai/dipilih user dalam website; (3) penyimpanan status aplikasi, seperti progres/update/aktivitas terakhir yang dilakukan user pada website tersebut.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Step 1: membuat fungsi dan form registrasi dengan cara mengimplementasikan fungsi bawaan dari Django.
Step 2: membuat fitur authentication yang meliputi log-in, log-out, dan sign-up.
Step 3: menambahkan restriksi yang memastikan user harus log-in sebelum bisa mengakses page website.
Step 4: menambahkan cookies untuk mencatat data user yang log-in dan log-out.
Step 5: menghubungkan product dengan user sehingga setiap user bisa memiliki product yang unik.

