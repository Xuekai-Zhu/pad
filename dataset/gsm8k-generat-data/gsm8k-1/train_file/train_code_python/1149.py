def solution():
    """A driver travels 30 miles per hour for 3 hours and 25 miles per hour for 4 hours to deliver goods to a town every day from Monday to Saturday.
    How many miles does the driver travel in a week?"""
    monday_to_saturday = 6
    distance_first_leg = 30 * 3
    distance_second_leg = 25 * 4
    total_distance = (distance_first_leg + distance_second_leg) * monday_to_saturday
    result = total_distance
    return result

print(solution())