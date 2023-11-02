def solution():
    """Tod drives his family car 55 miles to the north and 95 miles to the west.
    If Tod constantly drives 25 miles an hour the entire trip how many hours did Tod drive?"""
    # Calculate the total distance traveled
    total_distance = 55 + 95

    # Calculate the time taken to travel the total distance at a constant speed of 25 mph
    time_taken = total_distance / 25

    # Round off the time taken to the nearest hundredth
    time_taken = round(time_taken, 2)

    # Return the result
    result = time_taken
    return result

print(solution())