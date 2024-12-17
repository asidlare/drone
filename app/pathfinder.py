import logging
from typing import Annotated

from app.transmitter import Transmitter, TransmittersGraph
from app.utils import PositiveInt, CircleUtils

logging.basicConfig(level=logging.DEBUG)


class Pathfinder(PositiveInt):
    __slots__ = ('x_start', 'y_start', 'x_end', 'y_end')

    def __init__(self, x_start: int, y_start: int, x_end: int, y_end: int) -> None:
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end

        logging.info(f"Added coordinates of the initial point ({x_start}, {y_start})")
        logging.info(f"Added coordinates of the final point ({x_end}, {y_end})")

        # circle utils with helper methods for two circles
        # in the Cartesian coordinate system
        self.circle_utils = CircleUtils()

        # adjacent dict to hold dependencies between transmitters
        self.transmitters = dict()
        # initial and final set
        self._initial_transmitters = set()
        self._final_transmitters = set()

    @property
    def initial_transmitters(self) -> set:
        return self._initial_transmitters

    @initial_transmitters.setter
    def initial_transmitters(self, transmitter: Transmitter) -> None:
        if self.circle_utils.point_belongs_to_circle(
                x=transmitter.x,
                y=transmitter.y,
                r=transmitter.r,
                x_point=self.x_start,
                y_point=self.y_start
        ):
            self._initial_transmitters.add(transmitter)

    @property
    def final_transmitters(self) -> set:
        return self._final_transmitters

    @final_transmitters.setter
    def final_transmitters(self, transmitter: Transmitter) -> None:
        if self.circle_utils.point_belongs_to_circle(
                x=transmitter.x,
                y=transmitter.y,
                r=transmitter.r,
                x_point=self.x_end,
                y_point=self.y_end
        ):
            self._final_transmitters.add(transmitter)

    def add_transmitters_graph(self, transmitters_graph: TransmittersGraph) -> None:

        self.transmitters = transmitters_graph.transmitters
        # check if any transmitters defined
        self._check_if_transmitters_defined()
        # define initial and final sets
        self._define_initial_and_final_transmitters()


    def _check_if_transmitters_defined(self) -> None:
        if not self.transmitters:
            raise ValueError("No transmitters defined")
        # if new transmitters graph is added,
        # initial and final transmitters sets should be resetted
        self._initial_transmitters = set()
        self._final_transmitters = set()

    def _define_initial_and_final_transmitters(self) -> None:
        for transmitter in self.transmitters:
            # add to initial transmitters
            self.initial_transmitters = transmitter

            # add to final transmitters
            self.final_transmitters = transmitter

    # recursive method used by depth first search algorithm
    # it is modified to stop when it will meet any transmitter
    # which includes destination point
    def _dfs_util(self, transmitter: Transmitter, visited: set) -> None:
        # mark current raw as visited and print it
        visited.add(transmitter)
        logging.info(f"Visited... {transmitter}")

        # search all adjacent transmitters
        for neighbour in self.transmitters[transmitter]:
            # stops if destination point is found
            if self._check_if_final_trasmitter_in_visited(visited):
                return
            if neighbour not in visited:
                self._dfs_util(neighbour, visited)

    def _dfs_single(self, transmitter: Transmitter) -> set:
        # create a set for visited transmitters
        visited = set()

        self._dfs_util(transmitter, visited)
        return visited

    def _check_if_final_trasmitter_in_visited(self, visited: set) -> bool:
        for transmitter in self.final_transmitters:
            if transmitter in visited:
                return True
        return False

    def is_path_safe(self) -> bool:
        # if there is no transmitter which includes start or destination point,
        # it is not possible to fly
        if not self.initial_transmitters or not self.final_transmitters:
            return False
        # dfs must be executed for each transmitter which includes start point
        for initial_transmitter in self.initial_transmitters:
            visited = self._dfs_single(initial_transmitter)
            # it is possible to reach the destination if one of transmitters,
            # which include destination point, is reached
            if self._check_if_final_trasmitter_in_visited(visited):
                return True
        return False


# helper method which simplifies pathfinder algorithm
def drone_pathfinder(
        start_point: Annotated[list[int], 2],
        end_point: Annotated[list[int], 2],
        transmitters: list[Transmitter]
) -> str:
    # new transmitters graph object created
    transmitters_graph = TransmittersGraph()
    # transmitters are added
    for transmitter in transmitters:
        transmitters_graph.add_transmitter(transmitter)

    # new pathfinder instance is created
    pathfinder = Pathfinder(*start_point, *end_point)
    # transmitters are defined
    pathfinder.add_transmitters_graph(transmitters_graph)
    # result is found
    not_safe = 'The flight is not possible.'
    safe = 'The flight is safe.'
    result = pathfinder.is_path_safe()
    return safe if result else not_safe
