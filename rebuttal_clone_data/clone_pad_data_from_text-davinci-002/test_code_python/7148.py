def solution():
    start_koi_fish = 200
    start_goldfish = 80
    total_fish = start_koi_fish + start_goldfish
    koi_fish_added = 2
    goldfish_added = 5
    added_fish = koi_fish_added + goldfish_added
    fish_after_3_weeks = total_fish + (added_fish * 21)
    koi_fish_after_3_weeks = fish_after_3_weeks - 200
    result = koi_fish_after_3_weeks
    return result

print(solution())