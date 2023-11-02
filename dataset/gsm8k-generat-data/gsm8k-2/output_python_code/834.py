def solution():
    """Lana and her friends go to a theater on the weekend to watch a new play Joan told them was live. When they arrived, Lana saw 100 cars in the front parking lot. She saw two times more vehicles at the back than there were in the front parking lot. If the total number of cars at the end of the play was 700, how many more cars packed into the parking lot during the play?"""
    front_cars = 100
    back_cars = 2 * front_cars
    total_cars_at_start = front_cars + back_cars
    total_cars_at_end = 700
    cars_added_during_play = total_cars_at_end - total_cars_at_start
    result = cars_added_during_play
    return result

print(solution())