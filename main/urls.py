from django.urls import path
from main.views import show_main, create_nft_entry, nft_detail, show_xml, show_json, show_xml_by_id, show_json_by_id

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-nft-entry', create_nft_entry, name='create_nft_entry'),
    path('nft/<int:nft_id>/', nft_detail, name='nft_detail'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]

