def solution():
    """Lana and her friends go to a theater on the weekend to watch a new play Joan told them was live. When they arrived, Lana saw 100 cars in the front parking lot. She saw two times more vehicles at the back than there were in the front parking lot. If the total number of cars at the end of the play was 700, how many more cars packed into the parking lot during the play?"""
    # Define the initial number of cars in the front parking lot
    front_cars = 100

    # Calculate the number of cars in the back parking lot
    back_cars = front_cars * 2

    # Calculate the initial total number of cars
    total_cars = front_cars + back_cars

    # Calculate the number of cars that parked during the play
    parked_cars = 700 - total_cars

    # Return the result
    result = parked_cars
    return result

print(solution())