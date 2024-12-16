import pytest
from app.pathfinder import drone_pathfinder

@pytest.mark.parametrize(
    "start_point, end_point, expected",
    [
        ([10, 19], [19, 14], "The flight is safe."),
        ([10, 19], [13, 19], "The flight is safe."),
        ([10, 19], [13, 6], "The flight is safe."),
        ([10, 19], [18, 19], "The flight is not possible."),
        ([1, 19], [19, 14], "The flight is not possible."),
        ([10, 19], [18, 19], "The flight is not possible."),
        ([1, 19], [18, 19], "The flight is not possible."),
    ]
)
def test_drone_pathfinder(start_point, end_point, expected, transmitters):
    result = drone_pathfinder(start_point, end_point, transmitters)
    assert result == expected


@pytest.mark.parametrize(
    "start_point, end_point",
    [
        ([10.1, 19], [19, 14]),
        ([10, 19.24], [19, 14]),
        ([10, 19], ['19', 14]),
        ([10, 19], [19, 'test']),
        ([10, 19], [19, 0]),
    ]
)
def test_drone_pathfinder_raises(start_point, end_point, transmitters):
    with pytest.raises(ValueError):
        drone_pathfinder(start_point, end_point, transmitters)
