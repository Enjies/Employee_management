from django.contrib import admin
from django.urls import path, include

# Описуємо головні URL-шляхи додатку employee_management
urlpatterns = [
    # URL-шлях для адміністративної панелі Django
    path('admin/', admin.site.urls),

    # URL-шляхи для додатку employees через API
    path('api/', include('employees.urls')),

    # Загальні URL-шляхи для додатку employees
    path('', include('employees.urls')),
]
