from django.contrib import admin
from django.urls import path

#from todos.views import todo_list
from todos.views import TodoListView, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoCompleteView

#arquivo de configuração das rotas do app com nomes que referenciam as paginas e metodos

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TodoListView.as_view(), name="todo_list"),
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
]
