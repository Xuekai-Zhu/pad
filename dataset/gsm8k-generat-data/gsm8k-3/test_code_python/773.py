def solution():
    """Amoli and Anayet must travel 369 miles together. Amoli drove 42 miles an hour for 3 hours and Anayet drove at 61 miles an hour for 2 hours. How many miles do they still need to travel?"""
    # Calculate the distance traveled by Amoli
    amoli_distance = 42 * 3

    # Calculate the distance traveled by Anayet
    anayet_distance = 61 * 2

    # Calculate the total distance traveled
    total_distance = amoli_distance + anayet_distance

    # Calculate the distance remaining
    distance_remaining = 369 - total_distance

    # Display the distance remaining
    result = distance_remaining
    return result

print(solution())