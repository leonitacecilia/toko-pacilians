from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect  
from main.forms import ProductForm
from main.models import Product

def show_main(request):
    product_entries = Product.objects.all()
    context = {
        'nama_aplikasi': 'Toko Pacilians',
        'nama_pembuat': 'Leonita Cecilia',
        'kelas': 'PBP A',
        'harga': 'Rp22.000/kg',
        'deskripsi': 'Sebagai buah khas Indonesia, Mangga Harum Manis dikenal sebagai buah yang disukai banyak orang karena rasanya yang manis. Namun ternyata, tidak hanya rasanya yang manis, Mangga Harum Manis juga mengandung sejumlah nutrisi penting bagi tubuh, lho! Nutrisi secara lengkapnya dapat dilihat pada tabel berikut ini ya, teman-teman!',
        'product_entries': product_entries
    }

    return render(request, "main.html", context)

def product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "product_entry.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")