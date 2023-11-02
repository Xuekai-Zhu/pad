def solution():
    days_fishing = 213
    fish_caught_per_day_fisherman1 = 3
    fish_caught_per_day_fisherman2 = 1
    total_fish_caught_fisherman1 = fish_caught_per_day_fisherman1 * days_fishing
    total_fish_caught_fisherman2 = fish_caught_per_day_fisherman2 * 30 + fish_caught_per_day_fisherman2 * 2 * 60 + fish_caught_per_day_fisherman2 * 4 * (days_fishing - 120)
    fish_difference = total_fish_caught_fisherman1 - total_fish_caught_fisherman2
    result = abs(fish_difference)
    
    return result

print(solution())