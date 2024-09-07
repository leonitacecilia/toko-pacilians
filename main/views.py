from django.shortcuts import render

def show_main(request):
    context = {
        'nama_aplikasi' : 'Toko Pacilians',
        'nama_pembuat': 'Leonita',
        'kelas': 'PBP A'
    }

    return render(request, "main.html", context)
