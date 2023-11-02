def solution():
    # Calculate the time it takes to fold the dough
    folding_time = 4 * 5

    # Calculate the time it takes to let the dough rest
    rest_time = 4 * 75

    # Calculate the total preparation time
    preparation_time = folding_time + rest_time + 10

    # Calculate the total time including baking
    total_time = preparation_time + 30

    # Convert the time to hours
    hours = total_time / 60

    result = hours
    return result

print(solution())