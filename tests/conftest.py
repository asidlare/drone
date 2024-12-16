import pytest

from app.transmitter import Transmitter


@pytest.fixture(scope='function')
def transmitters():
    return [
        Transmitter(6, 11, 4),
        Transmitter(8, 17, 3),
        Transmitter(19, 19, 2),
        Transmitter(19, 11, 4),
        Transmitter(15, 7, 6),
        Transmitter(12, 19, 4),
    ]
