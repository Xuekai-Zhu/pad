def solution():
    """Erica sees 9 butterflies in the garden. She sees one-third of them fly away. How many butterflies are left in the garden?"""
    initial_butterflies = 9
    butterflies_fly_away = initial_butterflies / 3
    butterflies_left = initial_butterflies - butterflies_fly_away
    result = butterflies_left
    return result

print(solution())