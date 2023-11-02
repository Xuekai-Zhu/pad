def solution():
    """In the post-apocalyptic wasteland, 1 lizard is worth 8 bottle caps, 3 lizards are worth 5 gallons of water, and 1 horse is worth 80 gallons of water. Marla can scavenge for 20 bottle caps each day, but needs to pay 4 bottle caps per night for food and shelter. How many days does it take Marla to collect all the bottlecaps she needs to buy a horse?"""
    caps_per_lizard = 8
    lizards_per_water = 3
    water_per_horse = 80
    caps_per_water = lizards_per_water * caps_per_lizard
    caps_per_horse = water_per_horse * caps_per_water
    caps_per_day = 20
    caps_per_night = 4
    total_caps_needed = caps_per_horse
    caps_per_day_after_expenses = caps_per_day - caps_per_night
    days_to_collect_caps = total_caps_needed / caps_per_day_after_expenses
    result = days_to_collect_caps
    return result

print(solution())