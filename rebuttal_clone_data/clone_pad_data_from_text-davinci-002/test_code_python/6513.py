def solution():
    fish_caught_per_hour = 7
    hours_fishing = 9
    fish_lost = 15
    total_fish_caught = fish_caught_per_hour * hours_fishing - fish_lost
    result = total_fish_caught
    return result

print(solution())