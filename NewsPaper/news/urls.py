from django.urls import path
# Импортируем созданные нами представления
from .views import PostsList, PostDetail, NewsSearch, NewsCreate, NewsDelete, NewsUpdate, logout_user, upgrade_me, \
    CategoryList, subscribe
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', PostsList.as_view(), name='posts'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', NewsSearch.as_view(), name='post_search'),
    path('create/', NewsCreate.as_view(), name='post_create'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='post_update'),
    path('article/create/', NewsCreate.as_view()),
    path('logout/', logout_user, name='logout_user'),
    path('upgrade/', upgrade_me, name='upgrade'),
    path('categories/<int:pk>/', CategoryList.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe/', subscribe, name='subscribe'),
]
