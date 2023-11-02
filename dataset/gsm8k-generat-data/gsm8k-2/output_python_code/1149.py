def solution():
    """A driver travels 30 miles per hour for 3 hours and 25 miles per hour for 4 hours to deliver goods to a town every day from Monday to Saturday. How many miles does the driver travel in a week?"""
    monday_to_friday_distance = 30 * 3 + 25 * 4
    saturday_distance = 30 * 3
    total_distance = monday_to_friday_distance * 5 + saturday_distance
    result = total_distance
    return result

print(solution())