def solution():
    """John is trying to save money by buying cheap calorie-dense food. He can buy 10 burritos for $6 that have 120 calories each. He could also buy 5 burgers that are 400 calories each for $8. How many more calories per dollar does he get from the burgers?"""
    burrito_price = 6
    burrito_calories = 120
    burger_price = 8
    burger_calories = 400
    burrito_calories_per_dollar = (10 * burrito_calories) / burrito_price
    burger_calories_per_dollar = (5 * burger_calories) / burger_price
    difference = burger_calories_per_dollar - burrito_calories_per_dollar
    result = difference
    return result

print(solution())