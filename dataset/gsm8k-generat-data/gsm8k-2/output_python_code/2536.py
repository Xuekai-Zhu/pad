def solution():
    """James buys a jar of hot sauce. Each serving is .5 ounces. He uses 3 servings every day. if the container is 2 ounces less than 1 quart how many days will it last?"""
    jar_size = 31.5 # (1 quart = 32 ounces, minus 2 ounces)
    servings_per_day = 3
    serving_size = 0.5
    daily_consumption = servings_per_day * serving_size
    days_of_supply = jar_size / daily_consumption
    result = days_of_supply
    return result

print(solution())