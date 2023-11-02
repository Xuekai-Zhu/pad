def solution():
    serving_size = 0.5  # in ounces
    servings_per_day = 3
    container_size = (32 - 2)  # in ounces
    # 1 quart = 32 ounces, and container is 2 ounces less than 1 quart

    # Calculate the total number of servings in the container
    total_servings = container_size / serving_size

    # Calculate the number of days the container will last
    num_days = total_servings / servings_per_day
    result = num_days
    return result

print(solution())