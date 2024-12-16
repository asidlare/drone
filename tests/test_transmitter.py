import pytest

from app.transmitter import Transmitter
from app.utils import CircleUtils


@pytest.mark.parametrize(
    "x, y, r",
    [
        (0, 1, 1),
        (1, -1, 5),
        (1, 1.2, 3),
        (1, 1, '1'),
        ('test', 2, 3),
        (1, 1, 2)
    ]
)
def test_transmitter_raises(x, y, r):
    with pytest.raises(ValueError):
        Transmitter(x, y, r)


def test_equal_transmitter():
    t1 = Transmitter(1, 1, 1)
    t2 = Transmitter(1, 1, 1)
    assert t1 == t2


@pytest.mark.parametrize(
    "x1, y1, r1, x2, y2, r2",
    [
        (4, 3, 3, 4, 3, 3),  # equal
        (4, 3, 3, 4, 3, 2),  # 2nd with smaller r, included
        (4, 3, 2, 4, 3, 3),  # 1st with smaller r, included
        (4, 3, 3, 3, 3, 2),  # different x, included
        (4, 3, 3, 5, 3, 2),  # different x included
        (10, 10, 3, 5, 10, 2),  # one point common
        (10, 10, 3, 6, 10, 2),  # more points common
    ]
)
def test_transmitters_with_range(x1, y1, r1, x2, y2, r2):
    t1 = Transmitter(x1, y1, r1)
    t2 = Transmitter(x2, y2, r2)
    assert t1 <= t2


def test_transmitter_out_of_range():
    t1 = Transmitter(10, 10, 3)
    t2 = Transmitter(3, 10, 2)
    assert t1 > t2
    assert t2 > t1


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (10, 10, True), # middle
        (9, 9, True),
        (10, 13, True),
        (12, 10, True),
        (5, 10, True),  # edge
        (10, 15, True),  # edge
        (15, 10, True),  # edge
        (10, 5, True),  # edge
        (4, 10, False),  # outside
        (4, 16, False), # outside
    ]
)
def test_point_within_a_transmitter(x, y, expected):
    t = Transmitter(10, 10, 5)
    assert CircleUtils().point_belongs_to_circle(t.x, t.y, t.r, x, y) is expected
