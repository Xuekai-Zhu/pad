def solution():
    squirrels_per_hour = 6
    rabbits_per_hour = 2
    calories_per_squirrel = 300
    calories_per_rabbit = 800

    # Calculate the total calories Brandon can get from catching squirrels in 1 hour
    total_squirrel_calories = squirrels_per_hour * calories_per_squirrel

    # Calculate the total calories Brandon can get from catching rabbits in 1 hour
    total_rabbit_calories = rabbits_per_hour * calories_per_rabbit

    # Calculate the difference in calories between catching squirrels and rabbits
    calorie_difference = total_squirrel_calories - total_rabbit_calories
    result = calorie_difference
    return result

print(solution())