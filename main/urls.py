from django.urls import path
from main.views import delete_nft_entry, edit_nft_entry, logout_user, show_main, create_nft_entry, nft_detail, show_xml, show_json, show_xml_by_token_id, show_json_by_token_id, register, login_user, view_json_ui, view_xml_ui, add_nft_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-nft-entry/', create_nft_entry, name='create_nft_entry'),
    path('nft/<int:nft_id>/', nft_detail, name='nft_detail'),
    path('create-mood-nft-ajax', add_nft_entry_ajax, name='add_nft_entry_ajax'),


    # API Endpoints
    path('api/xml/', show_xml, name='show_xml'),
    path('api/json/', show_json, name='show_json'),
    path('api/xml/<str:token_id>/', show_xml_by_token_id, name='show_xml_by_token_id'),
    path('api/json/<str:token_id>/', show_json_by_token_id, name='show_json_by_token_id'),

    # UI Routes for Viewing JSON and XML
    path('view/xml/', view_xml_ui, name='view_xml_ui'),
    path('view/json/', view_json_ui, name='view_json_ui'),

    # Auth route
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),

    # Edit and Delete Routes
    path('edit-nft/<int:nft_id>/', edit_nft_entry, name='edit_nft_entry'),
    path('delete-nft/<int:nft_id>/', delete_nft_entry, name='delete_nft_entry'),
]

