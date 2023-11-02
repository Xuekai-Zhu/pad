def solution():
    """Matteo traveled at 55 miles per hour for 4 hours. Shandy traveled at 45 miles per hour for 10 hours. How many miles farther did Shandy drive than Matteo?"""
    matteo_speed = 55
    matteo_time = 4
    shandy_speed = 45
    shandy_time = 10
    matteo_distance = matteo_speed * matteo_time
    shandy_distance = shandy_speed * shandy_time
    distance_diff = shandy_distance - matteo_distance
    result = distance_diff
    return result

print(solution())