def solution():
    """Sammy has 8 gifts to wrap. Each gift requires 1.5 meters of ribbon. Unfortunately, she has no available ribbon so Tom let her use his 15-meter long ribbon. How many meters of ribbon will be left from Tom's ribbon?"""
    num_gifts = 8
    ribbon_per_gift = 1.5
    total_ribbon_needed = num_gifts * ribbon_per_gift
    tom_ribbon = 15
    ribbon_left = tom_ribbon - total_ribbon_needed
    result = ribbon_left
    return result

print(solution())