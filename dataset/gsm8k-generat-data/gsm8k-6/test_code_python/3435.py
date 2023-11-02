def solution():
    # Calculate the calories per dollar for burritos and burgers
    burritos_calories = 10 * 120
    burgers_calories = 5 * 400
    burritos_price_per_calorie = 6 / burritos_calories
    burgers_price_per_calorie = 8 / burgers_calories

    # Calculate the difference in calories per dollar between burgers and burritos
    difference = burgers_price_per_calorie - burritos_price_per_calorie
    result = difference
    return result

print(solution())