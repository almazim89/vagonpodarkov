from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='index_url'),
	path('подарки', show_gifts, name='show_gifts_url'),
	path('классика/<str:slug>', cl_more, name='cl_more_url'),
	path('премиум/<str:slug>', pr_more, name='pr_more_url'),
	path('прайсы', prices_input, name='prices_input_url'),
	path('доставка', delivery_input, name='delivery_input_url'),
	path('контакты', contacts_input, name='contacts_input_url')
]