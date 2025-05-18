"""
Контроллер для обработки отправленных форм
"""
from flask import Blueprint, request, current_app, redirect, url_for, flash, render_template, jsonify
from app.models.form_data import ContactFormData
from app.utils.file_handlers import save_uploaded_files
from app.services.form_service import FormService

# Создаем Blueprint для обработки форм
form_bp = Blueprint('form', __name__)

@form_bp.route('/submit', methods=['POST'])
def submit():
    """
    Обработчик отправки формы
    
    Returns:
        str: Сообщение об успешной отправке
    """
    if request.method == 'POST':
        # Получаем данные формы
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')  # Получаем email (может быть пустым)
        description = request.form.get('description')
        pickup_address = request.form.get('pickup_address')
        delivery_address = request.form.get('delivery_address')
        pickup_date = request.form.get('pickup_date')
        pickup_time = request.form.get('pickup_time')
        loader = bool(request.form.get('loader'))
        notes = request.form.get('notes')
        
        # Обрабатываем загруженные файлы
        photos = request.files.getlist('photos')
        uploaded_files = save_uploaded_files(photos, current_app.config['UPLOAD_FOLDER'])
        
        # Создаем объект данных формы
        form_data = ContactFormData(
            name=name,
            phone=phone,
            email=email,
            description=description,
            pickup_address=pickup_address,
            delivery_address=delivery_address,
            pickup_date=pickup_date,
            pickup_time=pickup_time,
            loader=loader,
            notes=notes,
            photo_paths=uploaded_files
        )
        
        # Логируем данные для отладки
        print(f"Получены данные от {form_data.name} ({form_data.phone})")
        if form_data.email:
            print(f"Email для обратной связи: {form_data.email}")
        print(f"Перевозка от {form_data.pickup_address} до {form_data.delivery_address}")
        print(f"Дата и время: {form_data.pickup_date} {form_data.pickup_time}")
        
        # Email теперь отправляется через JavaScript, поэтому здесь только сохраняем данные
        # Здесь можно добавить сохранение данных в базу данных, если нужно
        
        return "Anfrage erfolgreich verarbeitet!" 