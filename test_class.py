from triangle_class import Triangle, IncorrectTriangleSides


def test_create_triangle():
    t = Triangle(3, 4, 5)
    assert t.a == 3
    assert t.b == 4
    assert t.c == 5


def test_triangle_type():
    t1 = Triangle(1, 1, 1)
    assert t1.triangle_type() == "equilateral"
    t2 = Triangle(3, 3, 4)
    assert t2.triangle_type() == "isosceles"
    t3 = Triangle(3, 4, 5)
    assert t3.triangle_type() == "nonequilateral"


def test_perimeter():
    t = Triangle(-1, 2, 3)
    assert t.perimeter() == 12


def test_incorrect_triangle_sides():
    try:
        t = Triangle(0, 0, 0)
    except IncorrectTriangleSides as e:
        assert str(e) == "IncorrectTriangleSides."


if __name__ == "__main__":
    test_create_triangle()
    test_triangle_type()
    test_perimeter()
    test_incorrect_triangle_sides()
