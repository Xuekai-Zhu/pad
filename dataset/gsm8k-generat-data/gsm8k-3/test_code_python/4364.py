def solution():
    """Jackson wants to improve his endurance running. His goal is to start by running 3 miles a day the first week, then spend the next four weeks running one additional mile/day each week. How many miles is Jackson running each day at the end of this exercise program?"""
    # Define the initial distance and increment
    initial_distance = 3
    increment = 1

    # Calculate the distances for each week
    week1_distance = initial_distance
    week2_distance = initial_distance + increment
    week3_distance = initial_distance + 2 * increment
    week4_distance = initial_distance + 3 * increment
    week5_distance = initial_distance + 4 * increment

    # Calculate the total distance
    total_distance = week1_distance + week2_distance + week3_distance + week4_distance + week5_distance

    # Calculate the average distance per day
    average_distance = total_distance / 35

    result = average_distance
    return result

print(solution())