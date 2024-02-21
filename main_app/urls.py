from django.urls import path
from .views import home_page, delete_post, edit_post


urlpatterns=[
    path('',home_page, name='home'), 
    path("post/<int:post_id>/", delete_post ,name="delete_post"), #this is the url that will be used to call the function delete_
    path("post/<int:post_id>/edit", edit_post ,name="edit_post"), #this is the url that will be used to call the function edit_
]