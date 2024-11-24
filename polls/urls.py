from django.urls import path,  include
from . import views
import debug_toolbar
from django.conf import settings
app_name = "polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

if settings.DEBUG:
    urlpatterns = [ 
        path('__debug__/', 
        include(debug_toolbar.urls)),
] + urlpatterns