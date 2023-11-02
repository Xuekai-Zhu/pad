def solution():
    """Jason is planning a parking garage that will have 12 floors. Every 3rd floor has a gate where drivers have to show ID, which takes two minutes. To get from one floor to the next, drivers have to drive 800 feet at 10 feet/second. How long, in seconds, does it take to get to the bottom of the garage from the top?"""
    # Define the number of floors in the garage
    floors = 12

    # Define the time to show ID at each gate
    gate_time = 2 * 60

    # Define the distance between each floor and the speed of the car
    floor_distance = 800
    car_speed = 10

    # Calculate the total time to go down the garage
    total_time = 0
    for floor in range(floors, 0, -1):
        # Add the time to go down one floor
        total_time += floor_distance / car_speed

        # Check if there is a gate on this floor
        if floor % 3 == 0:
            total_time += gate_time

    # Return the total time in seconds
    result = total_time
    return result

print(solution())