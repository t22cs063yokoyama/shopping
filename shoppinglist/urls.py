from django.urls import path
from .views import ItemList, ItemAddView, ItemShowView, ItemEditView, ItemDeleteView, ItemCheckView

app_name='shoppinglist'
urlpatterns = [
    path('list', ItemList.as_view(),name='list'),
    path('add', ItemAddView.as_view(), name='add'),
    path('show', ItemShowView.as_view(), name='show'),
    path('edit', ItemEditView.as_view(), name='edit'),
    path('delete', ItemDeleteView.as_view(), name='delete'),
    path('check', ItemCheckView.as_view(), name='check'),
    
]