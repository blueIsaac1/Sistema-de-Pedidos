from src.domains.product import Product

def test_should_create_Product():
    product: Product = Product(name='NoteBook', description="AIR M1", price=6000)
    assert product.name == 'NoteBook'
    assert product.description == 'AIR M1'
    assert product.price == 6000
