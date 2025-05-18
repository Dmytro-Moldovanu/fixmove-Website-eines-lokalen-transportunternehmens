"""
Конфигурационный файл приложения
"""
import os

class Config:
    """
    Базовый класс конфигурации
    """
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-dev-key')
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB максимальный размер загружаемых файлов
    # EmailJS настройки
    EMAILJS_USER_ID = os.environ.get('EMAILJS_USER_ID', 'HDkfTM23gfmDWw3oG')


class DevelopmentConfig(Config):
    """
    Конфигурация для разработки
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Конфигурация для production
    """
    DEBUG = False
    # В production среде SECRET_KEY должен быть установлен через переменные окружения 