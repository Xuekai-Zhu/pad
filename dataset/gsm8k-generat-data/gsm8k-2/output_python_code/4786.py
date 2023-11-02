def solution():
    """In the post-apocalyptic wasteland, 1 lizard is worth 8 bottle caps, 3 lizards are worth 5 gallons of water, and 1 horse is worth 80 gallons of water. Marla can scavenge for 20 bottle caps each day, but needs to pay 4 bottle caps per night for food and shelter. How many days does it take Marla to collect all the bottlecaps she needs to buy a horse?"""
    caps_per_lizard = 8
    lizards_per_gallon = 3
    gallons_per_horse = 80
    caps_per_day = 20
    nightly_expenses = 4
    horse_cost = gallons_per_horse * lizards_per_gallon * caps_per_lizard
    days_to_collect = (horse_cost / caps_per_day) + (nightly_expenses * 7)
    result = days_to_collect
    return result

print(solution())