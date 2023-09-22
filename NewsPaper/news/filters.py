from django_filters import FilterSet, CharFilter, DateFilter
from .models import Post
from django import forms


class PostFilter(FilterSet):
    title = CharFilter(lookup_expr='icontains', label='По заголовку')
    post_author__author__username = CharFilter(lookup_expr='icontains', label='По имени автора')
    date_created = DateFilter(field_name='date_created', lookup_expr='gt', widget=forms.DateInput(attrs={'type': 'date'}), label='Позже чем')

    class Meta:
        model = Post
        fields = ['title', 'post_author__author__username', 'date_created']
