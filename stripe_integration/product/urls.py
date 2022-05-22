from django.urls import path
from .views import (
    ItemLandingPageView,
    RetrieveCheckoutSessionView,
    SuccessView,
    CancelView
)

urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('item/<int:pk>/', ItemLandingPageView.as_view(), name='item'),
    path('buy/<int:pk>/', RetrieveCheckoutSessionView.as_view(), name='buy')
]