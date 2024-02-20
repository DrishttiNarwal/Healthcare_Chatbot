from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("<str:name>", views.greet, name="greet"),
    # path("brian", views.brian, name="brian"),
    # path("david", views.david, name="david"),
    # path("my-view/", views.my_view, name="my_view")
    path("form.html", views.form, name="form"),
    path("chatbot.html", views.chatbot, name="chatbot")
]
