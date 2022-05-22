import stripe
from django.conf import settings
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views import View
from .models import Item


stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = "success.html"


class CancelView(TemplateView):
    template_name = "cancel.html"


class ItemLandingPageView(TemplateView):
    template_name = "item_landing.html"

    def get_context_data(self, **kwargs):
        item_id = self.kwargs["pk"]
        item, create = Item.objects.get_or_create(
            id=item_id,
            name='Item {}'.format(item_id),
            description='Description of Item {}'.format(item_id),
            price=1000 + int(item_id)
        )
        context = super(ItemLandingPageView, self).get_context_data(**kwargs)
        context.update({
            "product": item,
            "STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY
        })
        return context


class RetrieveCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item, create = Item.objects.get_or_create(
            id=item_id,
            name='Item {}'.format(item_id),
            description='Description of Item {}'.format(item_id),
            price=1000 + int(item_id)
        )
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': item.price,
                            'product_data': {
                                'name': item.name,
                                'images': ['https://i.imgur.com/EHyR2nP.png'],
                            },
                        },
                        'quantity': 1,
                    },
                ],
                metadata={
                    "product_id": item.id
                },
                mode='payment',
                success_url='http://127.0.0.1:8000/success/',
                cancel_url='http://127.0.0.1:8000/cancel/',
            )
            return JsonResponse({
                'sessionId': checkout_session.id
            })
        except Exception as error:
            return JsonResponse({
                'error': str(error)
            })
