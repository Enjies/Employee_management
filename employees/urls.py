from django.urls import path
from .views import EmployeeSearchView

# Описуємо маршрути для додатку employees
urlpatterns = [
    # URL-шлях для пошуку співробітника, використовує EmployeeSearchView для обробки запитів
    path('employee_search/', EmployeeSearchView.as_view(), name='employee_search'),
]