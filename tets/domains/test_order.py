from src.domains.order import Order, OrderStatus, OrderStatusName, OrderItem, Customer
from src.domains.product import Product

def test_should_create_order():

    customer: Customer = Customer(name='Isaac', email='ct@gmail.com', address='São Paulo')

    status: OrderStatus = OrderStatus(name=OrderStatusName.ACOMPLISHED)
    assert status.name == OrderStatusName.ACOMPLISHED

    prod1: Product = Product(name="NoteBook", description="AIR M1", price=5000)
    assert prod1.name == "NoteBook"
    assert prod1.description == "AIR M1"
    assert prod1.price == 5000

    prod2: Product = Product(name="NoteBook", description="AIR M2", price=10000)
    assert prod2.name == "NoteBook"
    assert prod2.description == "AIR M2"
    assert prod2.price == 10000

    item1: OrderItem = OrderItem(product_id=prod1.id, price=prod1.price, quantity=1)
    item2: OrderItem = OrderItem(product_id=prod2.id, price=prod2.price, quantity=2)
    
    order: Order = Order(customer = customer)
    order.add_status(status)
    order.add_item(item1)
    order.add_item(item2)

    assert len(order.status) == 1
    assert order.status[0].name == OrderStatusName.ACOMPLISHED
    assert len(order.items) == 2

    # Em preparação
    status2: OrderStatus = OrderStatus(name=OrderStatusName.IN_PREPARATION)
    order.add_status(status2)
    assert len(order.status) == 2
    assert order.status[1].name == OrderStatusName.IN_PREPARATION

    # Enviado
    status3: OrderStatus = OrderStatus(name=OrderStatusName.SEND)
    order.add_status(status3)
    assert len(order.status) == 3
    assert order.status[2].name == OrderStatusName.SEND

    # Entregue
    status4: OrderStatus = OrderStatus(name=OrderStatusName.DELIVERED)
    order.add_status(status4)
    assert len(order.status) == 4
    assert order.status[3].name == OrderStatusName.DELIVERED

    # Finalizado
    status5: OrderStatus = OrderStatus(name=OrderStatusName.DONE)
    order.add_status(status5)
    assert len(order.status) == 5
    assert order.status[4].name == OrderStatusName.DONE

    # Teste preço

    assert order.total() == 25000
    # assert item1.product_id == prod1.id
    # assert item1.price == prod1.price