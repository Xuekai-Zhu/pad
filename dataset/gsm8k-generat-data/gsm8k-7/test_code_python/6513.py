def solution():
    fish_per_hour = 7
    hours_fishing = 9
    fish_lost = 15

    # Calculate the total number of fish Julio caught before losing some
    total_fish = fish_per_hour * hours_fishing

    # Calculate the total number of fish Julio has after losing some
    net_fish = total_fish - fish_lost
    result = net_fish
    return result

print(solution())