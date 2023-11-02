def solution():
    """Lana and her friends go to a theater on the weekend to watch a new play Joan told them was live. When they arrived, Lana saw 100 cars in the front parking lot. She saw two times more vehicles at the back than there were in the front parking lot. If the total number of cars at the end of the play was 700, how many more cars packed into the parking lot during the play?"""
    # Calculate the number of cars at the back parking lot
    back_cars = 2 * 100

    # Calculate the total number of cars at the beginning
    initial_cars = 100 + back_cars

    # Calculate the number of cars that arrived during the play
    ending_cars = 700
    during_play_cars = ending_cars - initial_cars

    # Display the number of cars that arrived during the play
    result = during_play_cars
    return result

print(solution())