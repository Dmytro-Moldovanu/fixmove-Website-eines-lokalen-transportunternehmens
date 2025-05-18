"""
Модель данных формы обратной связи
"""
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ContactFormData:
    """
    Класс для хранения данных формы обратной связи
    """
    name: str
    phone: str
    description: str
    pickup_address: str
    delivery_address: str
    pickup_date: str
    pickup_time: str
    loader: bool
    email: Optional[str] = None
    notes: Optional[str] = None
    photo_paths: List[str] = None
    
    def __post_init__(self):
        """
        Инициализация после создания объекта
        """
        if self.photo_paths is None:
            self.photo_paths = []
    
    def to_dict(self) -> dict:
        """
        Преобразование данных формы в словарь для сохранения или отправки
        
        Returns:
            dict: Словарь с данными формы
        """
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'description': self.description,
            'pickup_address': self.pickup_address,
            'delivery_address': self.delivery_address,
            'pickup_date': self.pickup_date,
            'pickup_time': self.pickup_time,
            'loader': self.loader,
            'notes': self.notes,
            'photo_paths': self.photo_paths
        } 