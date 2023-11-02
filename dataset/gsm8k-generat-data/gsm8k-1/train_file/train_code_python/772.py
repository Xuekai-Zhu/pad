def solution():
    """Amoli and Anayet must travel 369 miles together. Amoli drove 42 miles an hour for 3 hours and Anayet drove at 61 miles an hour for 2 hours. How many miles do they still need to travel?"""
    amoli_miles = 42 * 3
    anayet_miles = 61 * 2
    total_miles_traveled = amoli_miles + anayet_miles
    miles_left = 369 - total_miles_traveled
    result = miles_left
    return result

print(solution())