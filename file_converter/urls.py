from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_file, name="upload_pdf"),
    path("run_query/", views.run_query, name="run_query"),
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.add_client, name='add_client'),
    path('clients/edit/<int:client_id>/', views.edit_client, name='edit_client'),
    path('clients/delete/<int:client_id>/', views.delete_client, name='delete_client'),
    path('document_list/', views.document_list, name='document_list'),
    path('document_detail/<int:document_id>/', views.document_detail, name='document_detail'),

]
