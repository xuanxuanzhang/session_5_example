from src.calculations import sum


def test_simple_sum():
    a = 9
    b = 10
    a_plus_b = sum(a, b, a)

    # expected output
    a_plus_b_exp = 29

    assert a_plus_b_exp == a_plus_b