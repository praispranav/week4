from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'app1'
urlpatterns = [
    path("", views.index, name="Home"),
    path("car/<int:com_id>/", views.detail, name="detail"),
    path('about/', views.about , name="about"),
    path('contact/', views.contact, name="contact"),
    path(r'login/', views.login_request, name="login"),
    path(r'signup/', views.registration_request, name="signup"),
    path(r'logout/', views.logout_request, name="LogOut"),

    # path for contact us view

    # path for registration

    # path for login

    # path for logout

    # path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)