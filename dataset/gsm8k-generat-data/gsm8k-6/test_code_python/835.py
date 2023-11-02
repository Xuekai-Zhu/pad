def solution():
    # Calculate the number of cars parked at the back of the theater
    back_cars = 2 * 100

    # Calculate the total number of cars parked before the play
    initial_cars = 100 + back_cars

    # Calculate the number of cars parked at the end of the play
    final_cars = 700

    # Calculate the number of cars parked during the play
    parked_cars = final_cars - initial_cars
    result = parked_cars
    return result

print(solution())