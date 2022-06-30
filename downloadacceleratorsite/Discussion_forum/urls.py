from turtle import forward
from django.urls import path
from Discussion_forum.views import *

app_name = 'Discussion_forum' 
urlpatterns = [
    path('',home,name='home'),
    path('forward',forth,name='forward'),
    path('addindiscussion', addInQuestion,name='addInQuestion'),
    path('addinpost', addInAnswer,name='addInAnswer'),
    path('getforums', getForums, name='getforums'),
    path('forums/', forums, name='forums'),
    path('forums/<str:forumName>', forums, name='forums'),
    path('forums/<str:forumName>/<int:discussionId>', forums, name='forums'),
]