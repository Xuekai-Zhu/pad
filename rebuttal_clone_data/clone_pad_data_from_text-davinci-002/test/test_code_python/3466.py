def solution():
    horses = 4
    oats_per_horse_per_meal = 4
    grain_per_horse = 3
    meals_per_day = 2
    days = 3
    total_oats = horses * oats_per_horse_per_meal * meals_per_day * days
    total_grain = horses * grain_per_horse * days
    total_food = total_oats + total_grain
    result = total_food
    return result

print(solution())