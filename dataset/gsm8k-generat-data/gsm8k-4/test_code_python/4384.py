def solution():
    """For every 100 additional people that board a spaceship, its speed is halved. If the speed of the spaceship with 200 people on board is 500km per hour, what is its speed in km/hr when there are 400 people on board?"""
    # Define the initial speed and number of people on board
    initial_speed = 500
    initial_people = 200

    # Define the additional people and calculate the number of halvings
    additional_people = 400 - initial_people
    num_halvings = additional_people // 100

    # Calculate the final speed
    final_speed = initial_speed / (2 ** num_halvings)

    result = final_speed
    return result

print(solution())