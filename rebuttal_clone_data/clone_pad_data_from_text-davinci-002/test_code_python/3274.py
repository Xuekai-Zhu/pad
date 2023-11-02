def solution():
    fish_eaten_per_day = 2
    days_without_fish = 14
    fish_added = 8
    fish_lost = fish_eaten_per_day * days_without_fish
    fish_total = 60 - fish_lost + fish_added
    result = fish_total
    return result

print(solution())