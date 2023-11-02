def solution():
    """Jackson wants to improve his endurance running. His goal is to start by running 3 miles a day the first week, then spend the next four weeks running one additional mile/day each week. How many miles is Jackson running each day at the end of this exercise program?"""
    # Define the initial running distance
    distance = 3

    # Add an additional mile each week for the next four weeks
    for i in range(4):
        distance += 1

    # Calculate the total running distance at the end of the program
    total_distance = distance * 7

    # Calculate the average running distance per day
    average_distance = total_distance / 28

    # return the result
    result = average_distance
    return result

print(solution())