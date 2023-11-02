def solution():
    """Pamela reapplies an ounce of sunscreen every hour she's outside. Her sunscreen comes in 8-ounce bottles. While on vacation, if she will be outside 4 hours a day over 8 days, how many bottles of sunscreen will she need to pack?"""
    sunscreen_per_day = 4
    days = 8
    sunscreen_per_bottle = 8
    total_sunscreen = sunscreen_per_day * days
    bottles_needed = total_sunscreen / sunscreen_per_bottle
    result = bottles_needed
    return result

print(solution())