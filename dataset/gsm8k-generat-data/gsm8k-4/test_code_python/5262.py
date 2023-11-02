def solution():
    """Fabian went to a park to get some fresh air. He decided to walk there for 3 hours. Every hour he covers 5 kilometers. How many more hours did Fabian need to walk to reach a total of 30 kilometers?"""
    # Define the distance covered per hour
    distance_per_hour = 5

    # Define the total distance to cover
    total_distance = 30

    # Define the time already spent walking
    time_spent = 3

    # Calculate the distance already covered
    distance_covered = distance_per_hour * time_spent

    # Calculate the remaining distance to travel
    remaining_distance = total_distance - distance_covered

    # Calculate the remaining time needed to cover the remaining distance
    remaining_time = remaining_distance / distance_per_hour

    # Round up the remaining time to the nearest hour
    remaining_time = int(round(remaining_time))

    # Return the result
    result = remaining_time
    return result

print(solution())