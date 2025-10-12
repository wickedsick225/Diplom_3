# data.py
from faker import Faker

faker = Faker()

def generate_user():
    """Создаёт данные нового пользователя"""
    return {
        "email": faker.unique.email(),
        "password": faker.password(length=10),
        "name": faker.first_name()
    }
