from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator

# Модель Employee представляє співробітника з різними характеристиками
class Employee(models.Model):
    # Ім'я співробітника (не може містити цифри)
    full_name = models.CharField(max_length=255, validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Ім\'я не може містити цифри.')])

    # Номер телефону співробітника
    phone_number = models.CharField(max_length=15)

    # Електронна пошта співробітника (унікальна)
    email = models.EmailField(unique=True)

    # Ідентифікатор співробітника (унікальний)
    employee_id = models.CharField(max_length=10, unique=True)

    # Адреса співробітника
    address = models.TextField(blank=True, null=True)

    # Паспортні дані співробітника
    passport_data = models.CharField(max_length=20, blank=True, null=True)

    # Сімейний стан співробітника
    marital_status = models.CharField(max_length=10, choices=[('married', 'Одружений/заміжня'), ('single', 'Не одружений/не заміжня')], blank=True, null=True)

    # Робочі години співробітника на місяць
    working_hours_per_month = models.IntegerField(validators=[MinValueValidator(0)], blank=True, null=True)

    # Посада співробітника
    position = models.CharField(max_length=50, blank=True, null=True)

    # Зарплата співробітника
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], blank=True, null=True)

    def __str__(self):
        # Представлення об'єкта як рядка
        return self.full_name

    def get_employee_id(self):
        # Метод для отримання ідентифікатора співробітника
        return self.employee_id

