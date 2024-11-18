Tugas 9 Pemograman Berbasis Platform

Nama: Leonita Cecilia
NPM: 2306165710
Kelas: PBP-A
Kode Asdos: RZ

1. Jelaskan mengapa kita perlu membuat model untuk melakukan pengambilan ataupun pengiriman data JSON? Apakah akan terjadi error jika kita tidak membuat model terlebih dahulu?
Membuat model untuk pengambilan atau pengiriman data JSON diperlukan untuk memastikan data terstruktur dengan baik, mempermudah validasi, dan menjaga konsistensi selama proses pengolahan data. Tanpa model, pengelolaan data dapat menjadi lebih kompleks, rentan terhadap kesalahan seperti tipe data yang tidak sesuai, dan sulit untuk dikembangkan, meskipun secara teknis pengambilan dan pengiriman data JSON masih dapat dilakukan.
 
2. Jelaskan fungsi dari library http yang sudah kamu implementasikan pada tugas ini
Library 'http'' dalam Flutter digunakan untuk melakukan komunikasi dengan web service melalui HTTP request, seperti 'GET', 'POST', 'PUT', dan 'DELETE'. Fungsi utama library ini adalah memungkinkan aplikasi untuk mengakses data eksternal, mengirim data ke server, atau mengambil data dari server untuk ditampilkan dalam aplikasi. Dengan `http`, kita dapat mengirimkan request ke endpoint tertentu dan mengelola respons yang diterima, seperti mengkonversi data JSON ke model yang telah dibuat, sehingga mempermudah pengolahan dan penampilan data di aplikasi.

3. Jelaskan fungsi dari CookieRequest dan jelaskan mengapa instance CookieRequest perlu untuk dibagikan ke semua komponen di aplikasi Flutter.
'CookieRequest' berfungsi untuk mengelola HTTP request yang dilengkapi dengan mekanisme penyimpanan dan pengiriman cookie, memungkinkan autentikasi pengguna dan sesi yang konsisten antara klien dan server. Instance 'CookieRequest' perlu dibagikan ke semua komponen di aplikasi Flutter agar setiap bagian aplikasi dapat mengakses data sesi yang sama, seperti informasi login atau token autentikasi, sehingga mempermudah pengelolaan status pengguna tanpa perlu melakukan login ulang atau menyimpan data sesi secara manual di setiap komponen.
 
4. Jelaskan mekanisme pengiriman data mulai dari input hingga dapat ditampilkan pada Flutter.
Mekanisme pengiriman data pada Flutter dimulai dengan pengguna memasukkan data melalui widget input seperti 'TextField', yang kemudian dikirim ke server menggunakan HTTP request melalui library seperti 'http' atau 'CookieRequesr. Data ini biasanya dikirim dalam format JSON melalui metode seperti 'POST' untuk diproses oleh server. Setelah server memberikan respons, data yang diterima (juga dalam format JSON) dikonversikan ke dalam model Dart yang telah didefinisikan. Data yang telah diubah menjadi objek Dart ini kemudian ditampilkan di aplikasi menggunakan widget seperti 'FutureBuilder' untuk menampilkan hasil secara dinamis berdasarkan status respon dari server.

5. Jelaskan mekanisme autentikasi dari login, register, hingga logout. Mulai dari input data akun pada Flutter ke Django hingga selesainya proses autentikasi oleh Django dan tampilnya menu pada Flutter.
Mekanisme autentikasi dimulai dengan pengguna memasukkan data akun pada Flutter, seperti username dan password, yang dikirim ke server Django melalui HTTP request menggunakan metode 'POST'. Untuk proses register, Django memvalidasi data, membuat akun baru di database, dan memberikan respons berhasil atau gagal. Saat login, Django memverifikasi kredensial yang dikirim, membuat sesi, dan mengembalikan cookie atau token autentikasi ke Flutter melalui respons. Cookie atau token ini disimpan di aplikasi untuk autentikasi permintaan berikutnya. Untuk logout, Flutter mengirimkan permintaan ke Django untuk menghapus sesi atau token, sehingga akses ke fitur aplikasi terbatas. Setelah login berhasil, Flutter menggunakan cookie atau token untuk mengambil data dari server dan menampilkan menu atau halaman yang sesuai dengan status autentikasi pengguna.

6. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step! (bukan hanya sekadar mengikuti tutorial).
a. Melakukan authentikasi pada Django untuk Flutter dan membuat model kustom
b. Melakukan Fetch data dari Web Service pada Flutter (dengan cara menambahkan dependensi http untuk bertukar HTTP request, membuat model sesuai respons dari web service, mengirim HTTP request ke web service menggunakan http, mengonversi data dari web service ke model yang dibuat, dan menampilkan data dengan FutureBuilder).
c. State Management Dasar menggunakan Provider (Mengalokasikan resource menjadi lebih sederhana dan mengimplementasikan Flutter Devtool sehingga provider dapat dilacak dari Devtool)
d. Mengintegrasikan Form Flutter Dengan Layanan Django
e. Mengimplementasi Fitur Logout