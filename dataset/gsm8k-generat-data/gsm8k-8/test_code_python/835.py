def solution():
    # Calculate the initial number of car at the back parking lot
    back_parking_lot = 2 * 100

    # Calculate the total number of cars at the start
    total_start_cars = 100 + back_parking_lot

    # Calculate the number of cars that came in during the play
    cars_during_play = 700 - total_start_cars
    result = cars_during_play
    return result

print(solution())