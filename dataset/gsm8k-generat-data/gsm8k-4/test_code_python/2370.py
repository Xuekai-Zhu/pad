def solution():
    """Brandon can catch 6 squirrels or two rabbits in 1 hour. Each squirrel has 300 calories and each rabbit has 800 calories. How many more calories will he get per hour if he catches squirrels instead of rabbits?"""
    # Define the number of squirrels and rabbits that Brandon can catch in 1 hour
    squirrels_per_hour = 6
    rabbits_per_hour = 2

    # Define the number of calories in each squirrel and rabbit
    squirrel_calories = 300
    rabbit_calories = 800

    # Calculate the total number of calories Brandon can get by catching squirrels and rabbits for 1 hour
    total_calories_squirrels = squirrels_per_hour * squirrel_calories
    total_calories_rabbits = rabbits_per_hour * rabbit_calories

    # Calculate the difference in calories between catching squirrels and rabbits
    calorie_difference = total_calories_squirrels - total_calories_rabbits

    # Return the result
    result = calorie_difference
    return result

print(solution())