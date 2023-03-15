from django.urls import path
from .views import dates, HomeListViews, PostDetailView, CategoryListView, AuthorListView, PostCreateView, PostUpdateView, PostDeleteView, AboutPageView



urlpatterns = [
    # Pagina inicio
    path('', HomeListViews.as_view(), name='home'),

    # detalle de post
    path('post/<pk>', PostDetailView.as_view(), name='post'),

    # Filtrado por Categoría
    path('category/', CategoryListView.as_view(), name='category'),

    # filtrado de autor
    path('author/', AuthorListView.as_view(), name='author'),

    # Pagina filtrado por fecha
    path('dates/<int:month_id>/<int:year_id>', dates, name='dates'),

    # crear post
    path('create/', PostCreateView.as_view(), name='create'),

    # editar post
    path('update/<int:pk>', PostUpdateView.as_view(), name='update'),

    # Eliminar Post
    path('delete/<int:pk>', PostDeleteView.as_view(), name='delete'),

    # About ---- acerca de nosotros
    path('about/', AboutPageView.as_view(), name='about'),

]