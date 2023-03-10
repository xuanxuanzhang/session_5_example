from src.calculations import sum, product
def test_sum():
    a, b, c = 1, 2, 4
    assert 8 == sum(a, b, c, a)


def test_product():
    a, b, c = 1, 2, 4
    assert 9 == product(a, b, c, a)
#comment to test commit new