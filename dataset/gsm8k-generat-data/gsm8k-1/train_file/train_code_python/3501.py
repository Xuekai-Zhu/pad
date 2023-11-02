def solution():
    """Spike the bearded dragon eats crickets to get protein in his diet. He hunts 5 crickets every morning and three times that over the afternoon and evening, munching on leafy greens and other vegetation in between. How many crickets does Spike hunt per day?"""
    morning_hunt = 5
    afternoon_hunt = 3 * morning_hunt
    evening_hunt = 3 * morning_hunt
    total_hunt = morning_hunt + afternoon_hunt + evening_hunt
    result = total_hunt
    return result

print(solution())