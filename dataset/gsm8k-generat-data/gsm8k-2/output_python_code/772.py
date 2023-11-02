def solution():
    """Amoli and Anayet must travel 369 miles together. Amoli drove 42 miles an hour for 3 hours and Anayet drove at 61 miles an hour for 2 hours. How many miles do they still need to travel?"""
    amoli_distance = 42 * 3
    anayet_distance = 61 * 2
    total_distance = amoli_distance + anayet_distance
    remaining_distance = 369 - total_distance
    result = remaining_distance
    return result

print(solution())