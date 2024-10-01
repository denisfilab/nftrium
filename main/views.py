from fractions import Fraction
from typing import Tuple
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
from PIL import Image
import json
from django.utils.html import mark_safe
import xml.dom.minidom


@login_required(login_url='/login')
def show_main(request):
    images = [
        {'path': 'https://i.ibb.co.com/r37Bpxy/image1.png', 'price': '36', 'name': 'Sigma'},  
        {'path': 'https://i.ibb.co.com/1ZYsnYS/image2.jpg', 'price': '5', 'name': 'Rain of Roses'},     
        {'path': 'https://i.ibb.co.com/Z11NN8t/image3.jpg', 'price': '43', 'name': 'Noir Wanderer'},
        {'path': 'https://i.ibb.co.com/yYWc0Ww/image4.jpg', 'price': '69', 'name': 'Cosmic Leap'},  
        {'path': 'https://i.ibb.co.com/b2741sw/image5.png', 'price': '83', 'name': 'Alchemist Haven'}, 
        {'path': 'https://i.ibb.co.com/FhHSS43/image6.jpg', 'price': '76', 'name': 'Luminous Dreamscape'},  
        {'path': 'https://i.ibb.co.com/26MSNY0/image7.png', 'price': '20', 'name': 'Australian Koal'},    
        {'path': 'https://i.ibb.co.com/fXKh3gz/image8.png', 'price': '68', 'name': 'Luminous Dreamscape'},     
    ]
    
    nfts = NFT.objects.filter(user=request.user)

    # Iterate through each NFT to calculate adjusted dimensions
    for nft in nfts:
        try:
            with Image.open(nft.image.path) as img:
                original_width, original_height = img.size
                closest_ratio = find_closest_aspect_ratio(original_width, original_height)
                
                # Define adjusted dimensions based on the closest aspect ratio
                if closest_ratio == (5, 4):
                    adjusted_width, adjusted_height = 500 , 400
                elif closest_ratio == (16, 9):
                    adjusted_width, adjusted_height = 1600/3, 900/3
                elif closest_ratio == (4, 3):
                    adjusted_width, adjusted_height = 800/2, 600/2
                elif closest_ratio == (3, 4):
                    adjusted_width, adjusted_height = 600/2, 800/2
                elif closest_ratio == (9, 16):
                    adjusted_width, adjusted_height = 900/2, 1600/2
                else:
                    # Default dimensions if no ratio matches
                    adjusted_width, adjusted_height = original_width, original_height
                
                # Attach adjusted dimensions to the NFT object
                nft.adjusted_width = adjusted_width
                nft.adjusted_height = adjusted_height
        except Exception as e:
            # Handle exceptions (e.g., missing image)
            nft.adjusted_width = 800  # Default width
            nft.adjusted_height = 600  # Default height

    context = {
        'user': request.user,
        'nfts': nfts,
        'last_login': request.COOKIES.get('last_login', 'N/A'),
        'images': images,
        'count': nfts.count()
    }
    return render(request, "main.html", context)

def find_closest_aspect_ratio(width: int, height: int) -> Tuple[int, int]:
    aspect_ratios = [(5, 4), (16, 9), (4, 3), (3, 4), (9, 16)]
    original_ratio = Fraction(width, height).limit_denominator(16)
    
    def ratio_difference(ratio: Tuple[int, int]) -> float:
        return abs(original_ratio - Fraction(ratio[0], ratio[1]))
    
    closest_ratio = min(aspect_ratios, key=ratio_difference)
    return closest_ratio

def nft_detail(request, nft_id):
    # Retrieve the NFT object or return a 404 if not found
    nft = get_object_or_404(NFT, id=nft_id)

    context = {
        'nft': nft,
    }

    return render(request, 'nftcard.html', context)

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
        form = AuthenticationForm()
    
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
    
    return redirect('main:show_main')

# New UI Views
@login_required(login_url='/login')
def view_json_ui(request):
    nfts = NFT.objects.all()
    data = serializers.serialize('json', nfts)
    parsed = json.loads(data)
    formatted_json = json.dumps(parsed, indent=4)
    context = {
        'formatted_json': mark_safe(f"<pre>{formatted_json}</pre>")
    }
    return render(request, 'view_json.html', context)

# Somehow masi error, returnnya value dari xml aja, g ada teksnys
@login_required(login_url='/login')
def view_xml_ui(request):
    nfts = NFT.objects.all()
    
    data = serializers.serialize('xml', nfts)
    
    parsed_xml = xml.dom.minidom.parseString(data)
    pretty_xml = parsed_xml.toprettyxml(indent="  ")
    context = {
        'pretty_xml': pretty_xml
    }
    return render(request, 'view_xml.html', context)