from django.test import TestCase
from django.urls import reverse
from .models import Employee

# Тести для моделі Employee та відповідних переглядів
class EmployeeModelTest(TestCase):

    def test_employee_str_method(self):
        # Перевірка методу __str__ моделі Employee
        employee = Employee(full_name="Yehor", employee_id="EMP1")
        self.assertEqual(str(employee), "Yehor")

class EmployeeViewTest(TestCase):

    def setUp(self):
        # Налаштування для тестів переглядів
        self.employee = Employee.objects.create(
            full_name="Yehor",
            employee_id="EMP1",
            email="smth@gmail.com",
        )

    def test_employee_detail_view(self):
        # Тест для перегляду деталей співробітника
        url = reverse('employee_detail', args=[self.employee.employee_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Yehor")

    def test_employee_search_view(self):
        # Тест для перегляду пошуку співробітника
        url = reverse('employee_search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_employee_search_with_valid_id(self):
        # Тест для пошуку співробітника з дійсним ідентифікатором
        url = reverse('employee_search')
        data = {'employee_id': self.employee.employee_id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Yehor")
        # Додайте перевірку наявності інших даних на сторінці

    def test_employee_search_with_invalid_id(self):
        # Тест для пошуку співробітника з недійсним ідентифікатором
        url = reverse('employee_search')
        data = {'employee_id': 'invalid_id'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Employee not found.")
