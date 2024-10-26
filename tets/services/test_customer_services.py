from src.factories.customer_factory import CustomerFactory
from src.domains.customer import CustomerRegistration
from src.datalayer.repositories.mock.memdb import CUSTOMER_DB
from src.services.exceptions.customer_exceptions import ConfirmEmail
import pytest

@pytest.mark.asyncio
async def test_should_create_customer():
    service = CustomerFactory.create_mock()
    customer = CustomerRegistration(
        name = "Isaac",
        email = "ct@gmail.com",
        address = "São Paulo",
        password = '12345',
        confirm_password= '12345'
    )
    print(CUSTOMER_DB)
    response = await service.register(customer_registration=customer)
    print(response)

@pytest.mark.asyncio
async def test_should_raise_error_when_create_customer():
    service = CustomerFactory.create_mock()
    customer_error = CustomerRegistration(
        name = "Isaac",
        email = "ct@gmail.com",
        address = "São Paulo",
        password = '12345',
        confirm_password= '12345'
    )
    print(CUSTOMER_DB)

    with pytest.raises(ConfirmEmail) as e:
        await service.register(customer_registration=customer_error)
    
    assert str(e.value) == "E-mail ja cadastrado"
       