def solution():
    """Brandon can catch 6 squirrels or two rabbits in 1 hour. Each squirrel has 300 calories and each rabbit has 800 calories. How many more calories will he get per hour if he catches squirrels instead of rabbits?"""
    squirrels_per_hour = 6
    rabbits_per_hour = 2
    squirrel_calories = 300
    rabbit_calories = 800
    calories_from_squirrels = squirrels_per_hour * squirrel_calories
    calories_from_rabbits = rabbits_per_hour * rabbit_calories
    calorie_difference = calories_from_rabbits - calories_from_squirrels
    
    return calorie_difference

print(solution())