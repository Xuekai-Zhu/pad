def solution():
    total_distance = 20  # Arvin wants to run a total of 20 kilometers in a week
    days_per_week = 5  # Arvin runs for 5 days a week
    starting_distance = 2  # On the first day, Arvin ran 2 kilometers
    increment = 1  # Arvin increases his running distance by 1 kilometer each day

    # Calculate the total distance Arvin will run in 5 days
    total_distance_5_days = starting_distance + (starting_distance + increment) + (starting_distance + (2 * increment)) + (starting_distance + (3 * increment)) + (starting_distance + (4 * increment))

    # Calculate the distance Arvin ran on the 5th day
    distance_5th_day = total_distance - total_distance_5_days + (starting_distance + (4 * increment))
    result = distance_5th_day
    return result

print(solution())