def solution():
    """Mama bird has 6 babies in the nest. She needs to feed each baby 3 worms a day. Papa bird caught 9 worms. If she caught 13 worms and had 2 stolen, how many more does she need to catch to feed them for 3 days?"""
    baby_count = 6
    worms_per_baby = 3
    worms_needed_per_day = baby_count * worms_per_baby
    papa_bird_worms = 9
    mama_bird_worms = 13
    stolen_worms = 2
    total_worms = papa_bird_worms + mama_bird_worms - stolen_worms
    total_worms_needed = worms_needed_per_day * 3
    worms_to_catch = total_worms_needed - total_worms
    result = worms_to_catch
    return result

print(solution())