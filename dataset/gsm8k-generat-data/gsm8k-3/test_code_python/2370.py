def solution():
    """Brandon can catch 6 squirrels or two rabbits in 1 hour. Each squirrel has 300 calories and each rabbit has 800 calories. How many more calories will he get per hour if he catches squirrels instead of rabbits?"""
    # Calculate the total number of calories from 6 squirrels
    squirrel_calories = 6 * 300

    # Calculate the total number of calories from 2 rabbits
    rabbit_calories = 2 * 800

    # Calculate the difference in calories
    calorie_difference = rabbit_calories - squirrel_calories

    # Display the difference in calories
    result = calorie_difference
    return result

print(solution())