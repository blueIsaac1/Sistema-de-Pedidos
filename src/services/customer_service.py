from dataclasses import dataclass
from src.services.base import ServiceBase
from src.datalayer.interfaces import customer_repository_interface
from src.domains.customer import CustomerRegistration, Customer
from src.services.exceptions.customer_exceptions import ConfirmEmail

@dataclass
class CustomerService(ServiceBase):
    repository: customer_repository_interface

    async def register(self, customer_registration = CustomerRegistration) -> Customer:
        if await self.confirm_email(customer_registration.email):
            raise ConfirmEmail
        return await self.repository.register(customer_registration)

    async def confirm_email(self, email:str) -> bool:
        return await self.repository.confirm_email(email)