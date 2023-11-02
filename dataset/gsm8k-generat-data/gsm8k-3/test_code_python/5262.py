def solution():
    """Fabian went to a park to get some fresh air. He decided to walk there for 3 hours. Every hour he covers 5 kilometers. How many more hours did Fabian need to walk to reach a total of 30 kilometers?"""
    # Define the distance Fabian has already walked
    distance_walked = 5 * 3

    # Calculate the remaining distance to walk
    distance_remaining = 30 - distance_walked

    # Calculate the number of hours needed to walk the remaining distance
    hours_remaining = distance_remaining / 5

    # Display the number of hours remaining
    result = hours_remaining
    return result

print(solution())