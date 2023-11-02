def solution():
    daily_bottlecaps = 20
    bottlecaps_per_lizard = 8
    lizards_per_horse = 3
    horses_per_gallon_of_water = 1/80
    lizard_to_horse_ratio = lizards_per_horse * horses_per_gallon_of_water
    bottlescaps_needed_for_horse = bottlecaps_per_lizard * lizard_to_horse_ratio
    daily_expenses = 4
    bottlecaps_needed_for_expenses = daily_expenses * 7
    total_bottlecaps_needed = bottlescaps_needed_for_horse + bottlecaps_needed_for_expenses
    days_to_scavenge = total_bottlecaps_needed / daily_bottlecaps
    result = days_to_scavenge
    return result

print(solution())