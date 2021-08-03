from django.urls import path
from medicines.views import *

urlpatterns = [
    # path('test/', TestView.as_view()),
    # path('login/', LoginView.as_view()),
    path('', MedicineView.as_view()),
    path('types/', MedicineTypeListing.as_view())
]
