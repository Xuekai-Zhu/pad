def solution():
    """On a moonless night, three fireflies danced in the evening breeze. They were joined by four less than a dozen more fireflies, before two of the fireflies flew away. How many fireflies remained?"""
    initial_fireflies = 3
    more_fireflies = 4 + 12 - 4
    total_fireflies = initial_fireflies + more_fireflies
    flown_away_fireflies = 2
    remaining_fireflies = total_fireflies - flown_away_fireflies
    result = remaining_fireflies
    return result

print(solution())