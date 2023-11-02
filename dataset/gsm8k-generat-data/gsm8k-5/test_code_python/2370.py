def solution():
    squirrels_per_hour = 6  # Brandon can catch 6 squirrels in 1 hour
    rabbits_per_hour = 2  # Brandon can catch 2 rabbits in 1 hour
    squirrel_calories = 300  # Each squirrel has 300 calories
    rabbit_calories = 800  # Each rabbit has 800 calories

    # Calculate the total calories from catching squirrels in 1 hour
    squirrel_calories_per_hour = squirrels_per_hour * squirrel_calories

    # Calculate the total calories from catching rabbits in 1 hour
    rabbit_calories_per_hour = rabbits_per_hour * rabbit_calories

    # Calculate the difference in calories between catching squirrels and rabbits in 1 hour
    calorie_difference_per_hour = squirrel_calories_per_hour - rabbit_calories_per_hour

    result = calorie_difference_per_hour
    return result

print(solution())