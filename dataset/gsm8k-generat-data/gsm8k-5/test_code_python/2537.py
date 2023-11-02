def solution():
    servings_per_day = 3  # James uses 3 servings of hot sauce per day
    serving_size = 0.5  # Each serving of hot sauce is 0.5 ounces
    total_servings = (32 * 4) - 2  # The container is 2 ounces less than 1 quart (32 ounces)
    days_last = total_servings / (servings_per_day * serving_size)  # Calculate how many days the container will last

    result = days_last
    return result

print(solution())