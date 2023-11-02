def solution():
    # Calculate the total number of servings in the jar
    total_servings = (1 * 32 - 2) / 0.5  # container is 2 ounces less than 1 quart (32 ounces)
    # Calculate the number of days the jar will last
    days_last = total_servings / 3  # uses 3 servings every day
    result = days_last
    return result

print(solution())