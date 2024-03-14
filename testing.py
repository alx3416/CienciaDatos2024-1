import utils.processing as proc


def test_suma_valores_1(a=2, b=2):
    assert proc.suma_valores(a, b) == 4
