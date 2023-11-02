def solution():
    """John makes himself a 6 egg omelet with 2 oz of cheese and an equal amount of ham. Eggs are 75 calories each. Cheese is 120 calories per ounce. Ham is 40 calories per ounce. How many calories is the omelet?"""
    eggs = 6
    cheese = 2
    ham = 2
    egg_calories = eggs * 75
    cheese_calories = cheese * 120
    ham_calories = ham * 40
    total_calories = egg_calories + cheese_calories + ham_calories
    result = total_calories
    return result

print(solution())