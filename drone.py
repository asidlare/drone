from app.pathfinder import drone_pathfinder
from app.transmitter import Transmitter


def demo() -> None:
    t1 = Transmitter(6, 11, 4)
    t2 = Transmitter(8, 17, 3)
    t3 = Transmitter(19, 19, 2)
    t4 = Transmitter(19, 11, 4)
    t5 = Transmitter(15, 7, 6)
    t6 = Transmitter(12, 19, 4)

    start_point = [10, 19]
    end_point = [19, 14]

    result = drone_pathfinder(
        start_point=start_point,
        end_point=end_point,
        transmitters=[t1, t2, t3, t4, t5, t6]
    )
    print(f"\n{result}\n")


def read_from_input(
    input_str: str,
    input_length: int = 1,
    data_length: int = 1,
    is_transmitter_data: bool = False
) -> list[int] | list[Transmitter]:
    output_data = []
    print(f"\n{input_str}")
    while True:
        if len(output_data) == input_length:
            return output_data
        elif input_length > 1:
            print(f"Missing data: {input_length - len(output_data)}...")

        try:
            data = [int(val) for val in input().split() if int(val) > 0]
            if len(data) != data_length:
                raise ValueError("Incorrect data length.")
            if is_transmitter_data:
                output_data.append(Transmitter(*data))
            else:
                return data
        except ValueError:
            print("\nEnter correct data or press CTRL+C.")


if __name__ == '__main__':
    intro = '''
    
    '''

    print(f"{intro}\n")
    print("Below example demo:\n")
    demo()

    cnt = read_from_input(input_str="Enter the number of transmitters:")[0]
    transmitters = read_from_input(
        input_str="Enter the coordinates of center and the power of each transmitter "
                  "separated by spaces",
        input_length=cnt,
        data_length=3,
        is_transmitter_data=True
    )
    start_point = read_from_input(
        input_str="Enter the coordinates of the initial point separated by spaces",
        data_length=2
    )
    end_point = read_from_input(
        input_str="Enter the coordinates of the final point separated by spaces",
        data_length=2
    )

    result = drone_pathfinder(
        start_point=start_point,
        end_point=end_point,
        transmitters=transmitters
    )
    print(f"\n{result}")
