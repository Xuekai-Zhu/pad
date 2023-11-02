def solution():
    """Lana and her friends go to a theater on the weekend to watch a new play Joan told them was live. When they arrived, Lana saw 100 cars in the front parking lot. She saw two times more vehicles at the back than there were in the front parking lot.
    If the total number of cars at the end of the play was 700, how many more cars packed into the parking lot during the play?"""
    front_parking_lot = 100
    back_parking_lot = 2 * front_parking_lot
    total_cars = front_parking_lot + back_parking_lot
    cars_after_play = 700
    cars_in_lot_during_play = cars_after_play - total_cars
    result = cars_in_lot_during_play
    return result

print(solution())