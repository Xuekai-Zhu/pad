def solution():
    # Calculate the calories per dollar for the burritos
    burrito_calories = 120 * 10
    burrito_price = 6
    burrito_calories_per_dollar = burrito_calories / burrito_price

    # Calculate the calories per dollar for the burgers
    burger_calories = 400 * 5
    burger_price = 8
    burger_calories_per_dollar = burger_calories / burger_price

    # Calculate the difference in calories per dollar between the burgers and burritos
    calories_per_dollar_difference = burger_calories_per_dollar - burrito_calories_per_dollar
    result = calories_per_dollar_difference
    return result

print(solution())