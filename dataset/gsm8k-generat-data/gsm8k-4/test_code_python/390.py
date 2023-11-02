def solution():
    """Oscar wants to train for a marathon. He plans to add 2/3 of a mile each week until he reaches a 20-mile run. How many weeks before the marathon should he start training if he has already run 2 miles?"""
    # Define the starting distance and the target distance
    starting_distance = 2
    target_distance = 20

    # Define the distance increase per week
    distance_increase = 2/3

    # Initialize the week counter and the current distance
    weeks = 0
    current_distance = starting_distance

    # Increase the distance each week until the target distance is reached
    while current_distance < target_distance:
        weeks += 1
        current_distance += distance_increase

    # return the result
    result = weeks
    return result

print(solution())