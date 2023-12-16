from rest_framework import serializers
from .models import Employee

# Серіалізатор для моделі Employee, використовується для перетворення об'єктів Employee в JSON і навпаки
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        # Вказуємо модель, яку будемо серіалізувати
        model = Employee

        # Вказуємо всі поля моделі, які будуть включені в серіалізований об'єкт
        fields = '__all__'