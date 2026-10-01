
from django.urls import path
from django.conf.urls.static import static
from server import views
from django.conf import settings

urlpatterns = [

    # district
    path('district/',views.district),
    path('district_del/<int:did>/',views.district_del),
    path('district_edit/<int:uid>/',views.district_edit),

    # admin
    path('admin_registration/',views.admin_registration),
    path('admin_delete/<int:did>/',views.admin_delete),
    path('admin_edit/<int:eid>/',views.admin_edit),

    # place
    path('place/',views.place),
    path('place_delete/<int:did>/',views.place_delete),
    path('place_filter/<int:did>/',views.place_filter),
    path('place_edit/<int:eid>/',views.place_edit),

    # user
    path('user/',views.user),
    path('user_list/',views.user_list),
    path('login/',views.login),
    path('user_accept/<int:uid>/',views.user_accept),
    path('user_reject/<int:uid>/',views.user_reject),

    path('user_single/<int:uid>/',views.user_single),

    path('user_edit/<int:uid>/',views.user_edit),

    path('change_password/<int:uid>/',views.change_password),

    # login
    path('login/',views.login),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)