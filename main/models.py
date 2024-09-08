import hashlib
import uuid
from django.db import models

class NFT(models.Model):
    name = models.CharField(max_length=255)  
    price = models.IntegerField()  # Price in ETH
    description = models.TextField()  # Description of the NFT
    image = models.ImageField(upload_to='nfts/')  # Store in media/nfts folder
    creator = models.CharField(max_length=255)  # Creator of the NFT
    token_id = models.CharField(max_length=255, unique=True, blank=True, editable=False)  # Unique token identifier  using sha256
    created_at = models.DateTimeField(auto_now_add=True)  # When the NFT was created

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.token_id:  
            unique_string = f"{self.name}{uuid.uuid4()}{self.created_at}".encode('utf-8')
            self.token_id = hashlib.sha256(unique_string).hexdigest()
        super().save(*args, **kwargs) 

