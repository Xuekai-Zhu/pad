def solution():
    """Jeff’s work is 3 miles away. He walks there and back each day he works. How many miles does he walk if he has to work 5 times a week?"""
    distance_per_trip = 3 * 2  # Round trip
    days_per_week = 5
    total_distance = distance_per_trip * days_per_week
    result = total_distance
    return result

print(solution())