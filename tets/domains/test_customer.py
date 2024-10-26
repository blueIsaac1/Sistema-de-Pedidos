from src.domains.customer import Customer

def test_should_create_customer():
    customer: Customer = Customer(name='Isaac Cleiton', email='Isaac@gmail.com', address='São Paulo')
    assert customer.name == 'Isaac Cleiton'
    assert customer.email == 'Isaac@gmail.com'
    assert customer.address == 'São Paulo'