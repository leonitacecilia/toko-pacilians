from django.shortcuts import render

def show_main(request):
    context = {
        'nama_aplikasi': 'Toko Pacilians',
        'nama_pembuat': 'Leonita Cecilia',
        'kelas': 'PBP A',
        'harga': 'Rp22.000/kg',
        'deskripsi': 'Sebagai buah khas Indonesia, Mangga Harum Manis dikenal sebagai buah yang disukai banyak orang karena rasanya yang manis. Namun ternyata, tidak hanya rasanya yang manis, Mangga Harum Manis juga mengandung sejumlah nutrisi penting bagi tubuh, lho! Nutrisi secara lengkapnya dapat dilihat pada tabel berikut ini ya, teman-teman!',
        'nutrisi': {
            'Kalori': '99 kkal',
            'Protein': '1.4 gram',
            'Karbohidrat': '24.7 gram',
            'Lemak': '0.6 gram',
            'Serat': '2.6 gram',
            'Gula': '22.5 gram',
            'Vitamin C': '67% dari angka kebutuhan harian (DV)',
            'Tembaga': '20% dari DV',
            'Folat': '18% dari DV',
            'Vitamin B6': '12% dari DV',
            'Vitamin K': '6% dari DV',
            'Niasin': '7% dari DV',
            'Kalium': '6% dari DV',
            'Vitamin A': '10% dari DV',
            'Vitamin E': '10% dari DV',
            'Riboflavin': '5% dari DV',
            'Magnesium': '4% dari DV',
            'Tiamin': '4% dari DV'
        },
        'tingkat_kemanisan': '10/10'
    }

    return render(request, "main.html", context)
