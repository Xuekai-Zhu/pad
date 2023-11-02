def solution():
    """James buys a jar of hot sauce. Each serving is .5 ounces. He uses 3 servings every day. if the container is 2 ounces less than 1 quart how many days will it last?"""
    # Define the size of the jar in ounces
    jar_size = 32 - 2  # 1 quart = 32 ounces, minus 2 ounces for the smaller size jar

    # Define the amount of hot sauce used per day in ounces
    daily_usage = 3 * 0.5
    
    # Calculate the number of days the jar will last
    days = jar_size / daily_usage

    # Round down to the nearest whole number of days
    result = int(days)
    return result

print(solution())