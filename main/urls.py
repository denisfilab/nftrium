from django.urls import path
from main.views import logout_user, show_main, create_nft_entry, nft_detail, show_xml, show_json, show_xml_by_token_id, show_json_by_token_id, register, login_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-nft-entry', create_nft_entry, name='create_nft_entry'),
    path('nft/<int:nft_id>/', nft_detail, name='nft_detail'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:token_id>/', show_xml_by_token_id, name='show_xml_by_token_id'),
    path('json/<str:token_id>/', show_json_by_token_id, name='show_json_by_token_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]

