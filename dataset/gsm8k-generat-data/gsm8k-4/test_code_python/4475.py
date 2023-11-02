def solution():
    """If a vehicle is driven 12 miles on Monday, 18 miles on Tuesday, and 21 miles on Wednesday. What is the average distance traveled per day?"""
    # Define the distances traveled on each day
    distance_monday = 12
    distance_tuesday = 18
    distance_wednesday = 21

    # Calculate the total distance traveled
    total_distance = distance_monday + distance_tuesday + distance_wednesday

    # Calculate the average distance traveled per day
    average_distance = total_distance / 3

    # return the result
    result = average_distance
    return result

print(solution())