def solution():
    # Calculate the total amount of dog food needed per day
    total_weight = 20 + 40 + 10 + 30 + 50  # total weight of all the dogs
    total_food = total_weight / 10  # amount of dog food needed based on weight
    result = total_food
    return result

print(solution())