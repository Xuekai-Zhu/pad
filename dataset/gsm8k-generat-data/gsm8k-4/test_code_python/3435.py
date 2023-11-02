def solution():
    """John is trying to save money by buying cheap calorie-dense food. He can buy 10 burritos for $6 that have 120 calories each. He could also buy 5 burgers that are 400 calories each for $8. How many more calories per dollar does he get from the burgers?"""
    # Calculate the total calories in 10 burritos
    burrito_calories = 10 * 120

    # Calculate the calories per dollar for the burritos
    burrito_calories_per_dollar = burrito_calories / 6

    # Calculate the total calories in 5 burgers
    burger_calories = 5 * 400

    # Calculate the calories per dollar for the burgers
    burger_calories_per_dollar = burger_calories / 8

    # Calculate the difference in calories per dollar between the two options
    calories_per_dollar_difference = burger_calories_per_dollar - burrito_calories_per_dollar

    # Return the result
    result = round(calories_per_dollar_difference)
    return result

print(solution())