"""
Сервис для обработки данных форм
"""
from typing import Dict, Any, List
import json
import requests
from flask import current_app
from app.models.form_data import ContactFormData


class FormService:
    """
    Сервис для обработки данных форм
    """
    
    @staticmethod
    def process_form_data(form_data: ContactFormData) -> bool:
        """
        Обрабатывает данные формы, например сохраняет в базу данных
        или отправляет уведомление
        
        Args:
            form_data: Данные из формы
            
        Returns:
            bool: Результат обработки
        """
        # Логирование полученных данных
        print(f"Получены данные от {form_data.name} ({form_data.phone})")
        print(f"Перевозка от {form_data.pickup_address} до {form_data.delivery_address}")
        print(f"Дата и время: {form_data.pickup_date} {form_data.pickup_time}")
        
        # Отправка email уведомления
        email_result = FormService.send_email_notification(form_data)
        
        return email_result
    
    @staticmethod
    def send_email_notification(form_data: ContactFormData) -> bool:
        """
        Отправляет уведомление на email с данными из формы
        
        Args:
            form_data: Данные из формы
            
        Returns:
            bool: Результат отправки
        """
        try:
            # Данные для сервиса отправки email
            email_service_url = "https://api.emailjs.com/api/v1.0/email/send"
            service_id = "service_5ib3fgs"
            template_id = "template_ct7hwxz"
            recipient_email = "dmytro.moldovanu@gmail.com"
            public_key = "HDkfTM23gfmDWw3oG"
            
            # Подготовка данных для шаблона
            template_params = {
                'name': form_data.name,
                'phone': form_data.phone,
                'to_email': recipient_email,  # Используем to_email вместо reply_to
                'description': form_data.description,
                'pickup_address': form_data.pickup_address,
                'delivery_address': form_data.delivery_address,
                'pickup_date': form_data.pickup_date,
                'pickup_time': form_data.pickup_time,
                'loader': "Ja" if form_data.loader else "Nein",
                'notes': form_data.notes or "Keine Anmerkungen"
            }
            
            # Подготовка данных для запроса
            payload = {
                'service_id': service_id,
                'template_id': template_id,
                'user_id': public_key,  # Используем публичный ключ напрямую
                'template_params': template_params
            }
            
            # Отправка запроса на EmailJS API
            headers = {'Content-Type': 'application/json'}
            response = requests.post(
                email_service_url,
                data=json.dumps(payload),
                headers=headers
            )
            
            # Проверка ответа от сервера
            if response.status_code == 200:
                print(f"Email успешно отправлен на {recipient_email}")
                return True
            else:
                print(f"Ошибка при отправке email: {response.text}")
                return False
                
        except Exception as e:
            print(f"Исключение при отправке email: {str(e)}")
            return False 