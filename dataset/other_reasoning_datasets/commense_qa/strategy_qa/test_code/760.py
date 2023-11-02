def solution():
    ocelot_daily_food_range = range(600, 801)
    bee_hummingbird_weight = 2.5
    bee_hummingbird_daily_food = bee_hummingbird_weight * 1 #assuming 1 bee hummingbird per day
    if bee_hummingbird_daily_food in ocelot_daily_food_range:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())