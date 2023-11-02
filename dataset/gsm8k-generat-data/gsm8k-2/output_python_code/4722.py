def solution():
    """Cary walks 3 miles round-trip to the grocery store, where he buys and eats a candy bar with 200 calories. If Cary burns 150 calories per mile walked, what's Cary's net calorie deficit (expressed as a positive number)?"""
    distance = 3
    candy_calories = 200
    calorie_burn_per_mile = 150
    calorie_burn_total = distance * 2 * calorie_burn_per_mile
    net_calorie_deficit = calorie_burn_total - candy_calories
    result = net_calorie_deficit
    return result

print(solution())