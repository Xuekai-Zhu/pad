def solution():
    """Mabel is counting sharks in the ocean. She knows that of the fish that she sees, 25% will be sharks and 75% will be another type of fish. On day one she counts 15 fish. On day 2 she counts three times as many. How many sharks did she count over those two days?"""
    day_one_fish = 15
    day_two_fish = day_one_fish * 3
    total_fish = day_one_fish + day_two_fish
    total_sharks = total_fish * 0.25
    result = total_sharks
    return result

print(solution())