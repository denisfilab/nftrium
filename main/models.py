import hashlib
import uuid
from django.db import models
from django.contrib.auth.models import User


class NFT(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)  
    price = models.IntegerField()  # Price in ETH
    description = models.TextField()  # description
    image = models.ImageField(upload_to='nfts/')  # Store in media/nfts folder aka locaiton of the file
    creator = models.CharField(max_length=255)  # Creator of the NFT
    token_id = models.CharField(max_length=255, unique=True, blank=True, editable=False)  # uuid using sha256
    created_at = models.DateTimeField(auto_now_add=True)  # When the NFT was created

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.token_id:  
            unique_string = f"{self.name}{uuid.uuid4()}{self.created_at}".encode('utf-8')
            self.token_id = hashlib.sha256(unique_string).hexdigest()
        super().save(*args, **kwargs) 


