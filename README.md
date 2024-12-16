# drone
Playground for graph algorithms.
1. DFS implemented

To run tests, you have to run virtual environment for this repository.

### Running venv

Set python version for repo and set venv and activate.
```sh
$ pyenv install 3.12.7
$ pyenv local 3.12.7
$ python -m venv env
$ source env/bin/activate
```

### Install python dependencies in repo directory
```sh
pip install -U setuptools pip
pip install -e .
```

### Run tests
```sh
$ pytest -sv
```

# Project

* A remotely controlled drone is tested on a polygon (represented by the positive quadrant 
of the Cartesian coordinate system).
* A network of transmitters with different power, placed at different points of the polygon,
is used to control the device.
* The transmitters are represented by circles with center (x, y) and power (radius) r.
* A drone is controlled if it is within the range of at least one transmitter (the transmitters
must have at least one common point).
* The aim of the task is to determine whether the drone can safely fly between two given polygon
points - the initial and the final (both placed in the positive quadrant of the Cartesian
coordinate system).
* A flight is safe if there is a route, which is a continuous curve, from the initial point to the final point, running only through areas covered by the transmitters' range.

## Script `drone.py`

1. The number of transmitters n is read.
2. For each transmitter, its coordinates and power (x, y, r) are read.
3. The coordinates of the starting point (start_x, start_y) are read.
4. The coordinates of the ending point (end_x, end_y) are read.
5. The script returns the answer if there is a safe passage.

## Solution - steps

1. Transmitters were transformed into graph nodes in such a way that:
if the circles (ranges) contain, touch or intersect, they are considered neighboring nodes
in the graph.
2. Transmitters can be keys in the link graph, because the `__hash__` method has been implemented.
3. A graph of transmitters on the polygon has been created.
4. Each transmitter has been verified and the appropriate transmitters have been included
in the group of starting or ending nodes, depending on whether they contain a starting
or ending point.
5. If none of the transmitters contain a starting or ending point, then the flight is not possible.
6. The algorithm scans the graph starting from each of the starting transmitters
and checks whether any of the ending transmitters have been reached.
6. The algorithm stops (does not complete the full scan that DFS does) if any of the ending
transmitters is reached. The algorithm then declares that the flight is possible.
7. If no path is found in any DFS run, then the flight is not possible

## Sample run and logs

`python drone.py`

```bash
Enter the number of transmitters:
6

Enter the coordinates of center and the power of each transmitter separated by spaces
Missing data: 6...
6 11 4
Missing data: 5...
8 17 3
Missing data: 4...
19 19 2
Missing data: 3...
19 11 4
Missing data: 2...
15 7 6
Missing data: 1...
12 19 4

Enter the coordinates of the initial point separated by spaces
10 19

Enter the coordinates of the final point separated by spaces
19 14
INFO:root:Added... Transmitter: coordinates of the center -> (6, 11), power -> 4
INFO:root:Added... Transmitter: coordinates of the center -> (8, 17), power -> 3
INFO:root:Added... Transmitter: coordinates of the center -> (19, 19), power -> 2
INFO:root:Added... Transmitter: coordinates of the center -> (19, 11), power -> 4
INFO:root:Added... Transmitter: coordinates of the center -> (15, 7), power -> 6
INFO:root:Added... Transmitter: coordinates of the center -> (12, 19), power -> 4
INFO:root:Added coordinates of the initial point (10, 19)
INFO:root:Added coordinates of the final point (19, 14)
INFO:root:Visited... Transmitter: coordinates of the center -> (12, 19), power -> 4
INFO:root:Visited... Transmitter: coordinates of the center -> (8, 17), power -> 3
INFO:root:Visited... Transmitter: coordinates of the center -> (6, 11), power -> 4
INFO:root:Visited... Transmitter: coordinates of the center -> (15, 7), power -> 6
INFO:root:Visited... Transmitter: coordinates of the center -> (19, 11), power -> 4

The flight is safe.
```
