def solution():
    """Spike the bearded dragon eats crickets to get protein in his diet. He hunts 5 crickets every morning and three times that over the afternoon and evening, munching on leafy greens and other vegetation in between. How many crickets does Spike hunt per day?"""
    morning_crickets = 5
    afternoon_crickets = 3 * morning_crickets
    evening_crickets = 3 * morning_crickets
    total_crickets = morning_crickets + afternoon_crickets + evening_crickets
    result = total_crickets
    return result

print(solution())