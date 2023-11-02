def solution():
    """Mabel is counting sharks in the ocean. She knows that of the fish that she sees, 25% will be sharks and 75% will be another type of fish. On day one she counts 15 fish. On day 2 she counts three times as many. How many sharks did she count over those two days?"""
    day1_fish = 15
    day2_fish = 3 * day1_fish
    total_fish = day1_fish + day2_fish
    shark_percentage = 0.25
    shark_count = total_fish * shark_percentage
    result = shark_count
    return result

print(solution())