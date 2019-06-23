from django.contrib import admin
from django.urls import path, include, re_path
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^graphql$', GraphQLView.as_view(graphiql=True))
]
