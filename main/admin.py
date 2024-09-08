from django.contrib import admin
from .models import NFT

@admin.register(NFT)
class NFTAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image', 'creator', 'token_id', 'created_at')
