def solution():
    # Calculate the calories obtained by catching 6 squirrels or 2 rabbits in 1 hour
    squirrel_calories = 6 * 300  # each squirrel has 300 calories
    rabbit_calories = 2 * 800  # each rabbit has 800 calories

    # Calculate the difference in calories obtained by catching squirrels instead of rabbits
    difference = squirrel_calories - rabbit_calories
    result = difference
    return result

print(solution())