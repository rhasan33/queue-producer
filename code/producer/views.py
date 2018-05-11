import os
from django.views import View
from django.http import JsonResponse
from kombu import Connection

from .queues import order_queue, restaurant_queue
from .producers import transport_task


class CreateOrderQueue(View):
    def get(self, request):
        try:
            transport_task(
                'order-queue',
                order_queue,
                args=('Hasan'),
                kwargs={}
            )
            return JsonResponse({
                "success": True,
                "message": "order queue successfully created."
            }, status=200)
        except TypeError:
            return JsonResponse({
                "success": False
            }, status=400)
        except Exception as err:
            return JsonResponse({
                "success": False,
                "message": str(err)
            }, status=400)


class CreateRestaurantQueue(View):
    def get(self, request):
        try:
            transport_task(
                'restaurant-queue',
                restaurant_queue,
                args=('Amiya'),
                kwargs={}
            )
            return JsonResponse({
                "success": True,
                "message": "restaurant queue successfully created."
            }, status=200)
        except TypeError:
            return JsonResponse({
                "success": False
            }, status=400)
        except Exception as err:
            return JsonResponse({
                "success": False,
                "message": str(err)
            }, status=400)
