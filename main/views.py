from django.shortcuts import render

def show_main(request):
    context = {
        'nama_aplikasi' : 'Toko Pacilians',
        'nama_pembuat': 'Leonita Cecilia',
        'kelas': 'PBP A'
    }

    return render(request, "main.html", context)
