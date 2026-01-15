"""
Konfigurationsdatei der Anwendung
"""
import os

class Config:
    """
    Basis-Konfigurationsklasse
    """
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-dev-key')
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB maximale Größe der hochgeladenen Dateien


class DevelopmentConfig(Config):
    """
    Entwicklungskonfiguration
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Konfiguration für production
    """
    DEBUG = False
    # In der production-Umgebung muss SECRET_KEY über Umgebungsvariablen gesetzt werden 