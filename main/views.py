from django.shortcuts import render, redirect
from .models import NFT
from .forms import NFTForm
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    nfts = NFT.objects.all()  
    context = {
        'nfts': nfts  
    }
    return render(request, "main.html", context)

def nft_detail(request, nft_id):
    nft = NFT.objects.get(id=nft_id)
    return render(request, 'nftcard.html', {'nft': nft})


def create_nft_entry(request):
    if request.method == "POST":
        form = NFTForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = NFTForm()

    context = {'form': form}
    return render(request, "create_nft_entry.html", context)

# Return all NFTs in XML format
def show_xml(request):
    data = NFT.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Return all NFTs in JSON format
def show_json(request):
    data = NFT.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Return a specific NFT by ID in XML format
def show_xml_by_id(request, id):
    data = NFT.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Return a specific NFT by ID in JSON format
def show_json_by_id(request, id):
    data = NFT.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
