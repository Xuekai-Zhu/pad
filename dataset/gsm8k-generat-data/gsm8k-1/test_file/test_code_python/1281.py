def solution():
    """The recent floods in Mamou’s country have left many families without food or shelter. To help, Mamou has volunteered to distribute 1,360 meals to the affected families. She gave out 64 meals on Friday, 30 meals on Saturday, and 48 meals on Sunday. How many meals does she have left to distribute?"""
    total_meals = 1360
    meals_given = 64 + 30 + 48
    meals_left = total_meals - meals_given
    result = meals_left
    return result

print(solution())