from src.domains.customer import CustomerRegistration, Customer
from src.datalayer.base import RepositoryInterface

class CustomerRepositoryInterface(RepositoryInterface): 
    pass

    async def register(self, CustomerRegistration) -> Customer:
        raise NotImplementedError

    async def confirm_email(self, email:str) -> bool:
        raise NotImplementedError