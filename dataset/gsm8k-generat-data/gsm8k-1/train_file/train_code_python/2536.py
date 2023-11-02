def solution():
    """James buys a jar of hot sauce. Each serving is .5 ounces. He uses 3 servings every day. if the container is 2 ounces less than 1 quart how many days will it last?"""
    serving_size = 0.5
    servings_per_day = 3
    ounces_in_quart = 32
    container_size = ounces_in_quart - 2
    total_servings = container_size / serving_size
    days_last = total_servings / servings_per_day
    result = days_last
    return result

print(solution())