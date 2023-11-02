def solution():
    # Define the number of squirrels and rabbits Brandon can catch in 1 hour
    squirrels_per_hour = 6
    rabbits_per_hour = 2

    # Define the calorie count for a squirrel and a rabbit
    squirrel_calories = 300
    rabbit_calories = 800

    # Calculate the total calories Brandon can get in 1 hour by catching squirrels and rabbits
    total_calories_squirrels = squirrels_per_hour * squirrel_calories
    total_calories_rabbits = rabbits_per_hour * rabbit_calories

    # Calculate the difference in total calories between catching squirrels and rabbits
    difference_in_calories = total_calories_rabbits - total_calories_squirrels

    result = difference_in_calories
    return result

print(solution())