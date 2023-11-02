def solution():
    """Mama bird has 6 babies in the nest. She needs to feed each baby 3 worms a day. Papa bird caught 9 worms. If she caught 13 worms and had 2 stolen, how many more does she need to catch to feed them for 3 days?"""
    babies_in_nest = 6
    worms_per_baby_per_day = 3
    total_worms_needed = babies_in_nest * worms_per_baby_per_day * 3
    worms_caught_by_papa_bird = 9
    worms_caught_by_mama_bird = 13
    worms_stolen = 2
    worms_needed = total_worms_needed - (worms_caught_by_papa_bird + worms_caught_by_mama_bird - worms_stolen)
    result = worms_needed
    return result

print(solution())