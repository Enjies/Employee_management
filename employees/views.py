from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Employee

class EmployeeSearchView(View):
    # Вказуємо шаблон для відображення
    template_name = 'employee_search.html'

    def get(self, request, *args, **kwargs):
        # Обробка HTTP GET-запиту
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        # Обробка HTTP POST-запиту
        # Отримуємо значення employee_id з POST-даних форми
        employee_id = request.POST.get('employee_id', None)
        
        if employee_id:
            try:
                # Шукаємо співробітника за вказаним employee_id
                employee = Employee.objects.get(employee_id=employee_id)
                # Відображаємо деталі співробітника за допомогою шаблону 'employee_detail.html'
                return render(request, 'employee_detail.html', {'employee': employee})
            except Employee.DoesNotExist:
                # Обробка винятку, якщо співробітник не знайдений
                error_message = 'Employee not found.'
                return render(request, self.template_name, {'error_message': error_message})
        else:
            # Виводимо повідомлення про відсутність введеного employee_id
            error_message = 'Please enter Employee ID.'
            return render(request, self.template_name, {'error_message': error_message})