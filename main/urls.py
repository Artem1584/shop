from django.urls import path

from .views import index
from .views import other_page
from .views import BBLoginVievs
from .views import profile
from .views import BBLogoutView
from .views import ChangeUserInfoView
from .views import BBPasswordChangeView
from .views import RegisterUserView
from .views import RegisterDoneViev
from .views import user_activate
from .views import DeleteUserView
from .views import by_rubric
from .views import detail
from .views import profile_bb_detail
from .views import profile_bb_add
from .views import profile_bb_change
from .views import profile_bb_delete

app_name = 'main'
urlpatterns = [
    # Активация пользователя
    path('accounts/register/activate/<str:sign>/', user_activate,
         name='register_activate'),
     # Правка данных пользователя
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='profile_change'),
    # Выход с сайта
    path('accouts/logout/', BBLogoutView.as_view(), name='logout'),
    # Удаление пользователя
    path('accounts/profile/delete/', DeleteUserView.as_view(), name='profile_delete'),
    # Смена пароля
    path('accounts/password/change/', BBPasswordChangeView.as_view(), name='password_change'),
    # Изменение объявления
    path('accounts/profile/change/<int:pk>/', profile_bb_change,
                                              name='profile_bb_change'),
    # Удаление объявления
    path('accounts/profile/delete/<int:pk>/', profile_bb_delete,
                                              name='profile_bb_delete'),
    # Добавление объявления
    path('accounts/profile/add/', profile_bb_add, name='profile_bb_add'),
    # Личная страница объявления
    path('accounts/profile/<int:pk>/', profile_bb_detail, name='profile_bb_detail'),
    # Страница пользовательского профиля
    path('accounts/profile/', profile, name='profile'),
    # Отправляет сообщение о успешной регистрации.
    path('accounts/register/done/', RegisterDoneViev.as_view(), name='register_done'),
    # Регистрирует пользователя.
    path('accounts/register/', RegisterUserView.as_view(), name='register'),
    # Вход на сайт
    path('accounts/login/', BBLoginVievs.as_view(), name='login'),
    # Страница выбранного объявления
    path('<int:rubric_pk>/<int:pk>/', detail, name='detail'),
    # Вывод списка рубрик
    path('<int:pk>/', by_rubric, name='by_rubric'),
    # Вспомогательные веб-страницы
    path('<str:page>/', other_page, name='other'),
    # Главная страница
    path('', index, name='index'),
]