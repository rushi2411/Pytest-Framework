from faker import Faker

fake_data_generator = Faker()

def generate_fake_data():
    return {
        "first_name": fake_data_generator.first_name(),
        "last_name": fake_data_generator.last_name(),
        "email": fake_data_generator.email(),
        "password": fake_data_generator.password()
    }