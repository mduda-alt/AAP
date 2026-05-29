
import pytest
from product import Product


@pytest.fixture
def towar():
    return Product("Laptop", 2999.99, 10)


@pytest.mark.parametrize(
    "ile_dodac, oczekiwany_stan",
    [
        (0, 10),
        (1, 11),
        (5, 15),
        (20, 30),
    ]
)
def test_add_stock_rozne_wartosci(towar, ile_dodac, oczekiwany_stan):
    towar.add_stock(ile_dodac)

    assert towar.quantity == oczekiwany_stan


def test_add_stock_negative_raises(towar):
    with pytest.raises(ValueError):
        towar.add_stock(-3)


def test_remove_stock_positive(towar):
    towar.remove_stock(4)

    assert towar.quantity == 6


def test_remove_stock_all(towar):
    towar.remove_stock(10)

    assert towar.quantity == 0


def test_remove_stock_negative_raises(towar):
    with pytest.raises(ValueError):
        towar.remove_stock(-1)


def test_remove_stock_too_much_raises(towar):
    with pytest.raises(ValueError):
        towar.remove_stock(100)


def test_is_available_when_in_stock(towar):
    assert towar.is_available() is True


def test_is_not_available_when_empty():
    pusty = Product("Myszka", 79.99, 0)

    assert pusty.is_available() is False


def test_total_value(towar):
    assert towar.total_value() == pytest.approx(29999.90)


def test_price_cannot_be_negative():
    with pytest.raises(ValueError):
        Product("Podejrzany kabel", -5.0, 3)


def test_quantity_cannot_be_negative():
    with pytest.raises(ValueError):
        Product("Klawiatura", 150.0, -2)
