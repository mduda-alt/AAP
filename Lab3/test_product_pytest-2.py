
import pytest
from product import Product


@pytest.fixture
def product():
    return Product("Laptop", 100.0, 10)


@pytest.mark.parametrize(
    "percent, expected_price",
    [
        (0, 100.0),
        (50, 50.0),
        (100, 0.0),
    ]
)
def test_apply_discount(product, percent, expected_price):
    product.apply_discount(percent)

    assert product.price == pytest.approx(expected_price)


@pytest.mark.parametrize(
    "zly_procent",
    [
        -1,
        -20,
        101,
        150,
    ]
)
def test_apply_discount_wrong_percent_raises(product, zly_procent):
    with pytest.raises(ValueError):
        product.apply_discount(zly_procent)


def test_apply_discount_changes_price():
    rzecz = Product("Monitor", 200.0, 3)

    rzecz.apply_discount(25)

    assert rzecz.price == pytest.approx(150.0)
