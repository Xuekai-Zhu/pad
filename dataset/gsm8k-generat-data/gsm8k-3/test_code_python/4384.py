def solution():
    """For every 100 additional people that board a spaceship, its speed is halved. If the speed of the spaceship with 200 people on board is 500km per hour, what is its speed in km/hr when there are 400 people on board?"""
    # Define the initial speed and number of people
    initial_speed = 500
    initial_people = 200

    # Define the change in speed per 100 additional people
    speed_change = 0.5

    # Calculate the number of increments of 100 people
    increments = (400 - initial_people) // 100

    # Calculate the final speed
    final_speed = initial_speed
    for i in range(increments):
        final_speed *= speed_change

    # Display the final speed
    result = final_speed
    return result

print(solution())