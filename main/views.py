from django.shortcuts import get_object_or_404, render, redirect
from .models import NFT
from .forms import NFTForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    images = [
    {'path': 'image1.jpg', 'price': '36', 'name': 'Sigma'},  
    {'path': 'image2.jpg', 'price': '5', 'name': 'Rain of Roses'},     
    {'path': 'image3.jpg', 'price': '43', 'name': 'Noir Wanderer'},
    {'path': 'image4.jpg', 'price': '69', 'name': 'Cosmic Leap'},  
    {'path': 'image5.jpg', 'price': '83', 'name': 'Alchemist Haven'}, 
    {'path': 'image6.jpg', 'price': '76', 'name': 'Luminous Dreamscape'},  
    {'path': 'image7.jpg', 'price': '20', 'name': 'Australian Koal'},    
    {'path': 'image8.jpg', 'price': '68', 'name': 'Luminous Dreamscape'},     
    ]
    nfts = NFT.objects.filter(user=request.user)
    context = {
        'user': request.user,
        'nfts': nfts,
        'last_login': request.COOKIES['last_login'],
        'images': images,
    }
    return render(request, "main.html", context)



def nft_detail(request, nft_id):
    nft = NFT.objects.get(id=nft_id)
    return render(request, 'nftcard.html', {'nft': nft})

def create_nft_entry(request):
    if request.method == "POST":
        form = NFTForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            nft = form.save(commit=False)
            nft.user = request.user
            nft.save()
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
def show_xml_by_token_id(request, token_id):
    data = NFT.objects.filter(token_id=token_id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Return a specific NFT by ID in JSON format
def show_json_by_token_id(request, token_id):
    data = NFT.objects.filter(token_id=token_id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def edit_nft_entry(request, nft_id):
    nft = NFT.objects.get(id=nft_id, user=request.user)
    
    if request.method == "POST":
        form = NFTForm(request.POST, request.FILES, instance=nft)
        if form.is_valid():
            form.save()
            messages.success(request, 'NFT Anda telah berhasil diperbarui!')
            return redirect('main:show_main')
    else:
        form = NFTForm(instance=nft)
    
    context = {'form': form, 'nft': nft}
    return render(request, "edit_nft_entry.html", context)

@login_required(login_url='/login')
def delete_nft_entry(request, nft_id):
    nft = get_object_or_404(NFT, id=nft_id, user=request.user)
    
    if request.method == "POST":
        nft.delete()
        messages.success(request, 'NFT Anda telah berhasil dihapus!')
        return redirect('main:show_main')
    
    # Tidak perlu render halaman delete karena menggunakan modal
    return redirect('main:show_main')