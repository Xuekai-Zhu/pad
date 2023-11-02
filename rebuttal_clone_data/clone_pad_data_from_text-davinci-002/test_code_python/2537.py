def solution():
    servings_per_day = 3
    ounces_per_serving = 0.5
    total_ounces = servings_per_day * ounces_per_serving
    containers_per_quart = 4
    container_size = containers_per_quart - 2
    days_per_container = container_size / total_ounces
    result = days_per_container
    return result

print(solution())