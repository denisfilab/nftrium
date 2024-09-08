from django.shortcuts import render
from .models import NFT  # Import your NFT model

def show_main(request):
    nfts = NFT.objects.all()  
    context = {
        'nfts': nfts  
    }
    return render(request, "main.html", context)

def nft_detail(request, nft_id):
    nft = NFT.objects.get(id=nft_id)  # Fetch the NFT object by its id
    return render(request, 'nftcard.html', {'nft': nft})
