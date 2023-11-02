def solution():
    # Calculate the number of bottle caps needed to buy a horse
    horse_cost = 80 * (3 / 5) * 8
    bottle_caps_needed = horse_cost / 8

    # Calculate the number of bottle caps Marla can collect in a day
    bottle_caps_per_day = 20

    # Calculate the number of bottle caps Marla spends on food and shelter each night
    bottle_caps_per_night = 4

    # Calculate the number of days it takes for Marla to collect enough bottle caps
    bottle_caps_collected = 0
    days = 0
    while bottle_caps_collected < bottle_caps_needed:
        bottle_caps_collected += bottle_caps_per_day
        bottle_caps_collected -= bottle_caps_per_night
        days += 1

    result = days
    return result

print(solution())