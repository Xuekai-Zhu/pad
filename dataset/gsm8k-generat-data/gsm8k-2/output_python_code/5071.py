def solution():
    """Erica sees 9 butterflies in the garden. She sees one-third of them fly away. How many butterflies are left in the garden?"""
    initial_butterflies = 9
    flown_away_butterflies = initial_butterflies / 3
    remaining_butterflies = initial_butterflies - flown_away_butterflies
    result = remaining_butterflies
    return result

print(solution())