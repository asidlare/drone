import logging
from functools import total_ordering

from app.utils import CircleUtils, PositiveInt

logging.basicConfig(level=logging.DEBUG)


@total_ordering
class Transmitter(PositiveInt):
    __slots__ = ('x', 'y', 'r')

    def __init__(self, x: int, y: int, r: int) -> None:
        if (x - r) < 0 or (y - r) < 0:
            raise ValueError("Transmitter cannot be negative")
        self.x = x
        self.y = y
        self.r = r

        # circle methods
        self.circle_utils = CircleUtils()

    # hash method to enable adding transmitters to adjacent dict
    def __hash__(self) -> int:
        return hash((self.x, self.y, self.r))

    def __eq__(self, other: object) -> bool:
        return (
            self.circle_utils.distance(x1=self.x, y1=self.y, x2=other.x, y2=other.y) == 0
            and self.r == other.r
        )

    def __lt__(self, other: object) -> bool:
        '''
        Includes:
            * externally tangent circles
            * internally tangent circles
            * internally disjoint circles
            * circles intersecting at two points
            * concentric circles
        '''
        return (
            self.circle_utils.r_diff(r1=self.r, r2=other.r)
            <= self.circle_utils.distance(x1=self.x, y1=self.y, x2=other.x, y2=other.y)
            <= self.circle_utils.r_sum(r1=self.r, r2=other.r)
            or self.circle_utils.distance(x1=self.x, y1=self.y, x2=other.x, y2=other.y) == 0
        )

    def __repr__(self) -> str:
        return (f"Transmitter: coordinates of the center -> ({self.x}, {self.y}), "
                f"power -> {self.r}")


class TransmittersGraph:
    def __init__(self) -> None:
        self._transmitters = {}

    @property
    def transmitters(self) -> dict:
        return self._transmitters

    def add_transmitter(self, transmitter: Transmitter) -> None:
        # if a transmitter with exactly the same x, y and r exists
        # there is no reason to add it again
        if transmitter in self._transmitters:
            return

        # add empty list for this transmitter
        self._transmitters[transmitter] = []
        # new list of existing created
        existing_transmitters = list(self._transmitters.keys())
        # iterating over the list
        for prev_transmitter in existing_transmitters:
            if prev_transmitter <= transmitter:
                self._transmitters[prev_transmitter].append(transmitter)
                self._transmitters[transmitter].append(prev_transmitter)

        logging.info(f"Added... {transmitter}")
