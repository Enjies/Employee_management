from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    # Відображення полів моделі у списку записів
    list_display = ('full_name', 'phone_number', 'email', 'employee_id', 'address', 'passport_data', 'marital_status', 'working_hours_per_month', 'position', 'salary')

    # Поля, за якими можна виконувати пошук
    search_fields = ['full_name', 'email', 'employee_id']

# Реєстрація моделі Employee в адміністративній панелі з використанням налаштувань EmployeeAdmin
admin.site.register(Employee, EmployeeAdmin)