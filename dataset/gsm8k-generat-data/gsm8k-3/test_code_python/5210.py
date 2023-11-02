def solution():
    """There is 80 mg of caffeine in a cup of coffee. Lisa does not want to drink more than 200 mg of caffeine per day. If she drinks three cups of coffee, how many milligrams of coffee did Lisa drink over her goal?"""
    # Define the caffeine content per cup of coffee
    CAFFEINE_PER_CUP = 80

    # Define Lisa's daily caffeine limit
    DAILY_LIMIT = 200

    # Calculate the total caffeine content of the three cups of coffee
    total_caffeine = CAFFEINE_PER_CUP * 3

    # Calculate the excess caffeine consumption, if any
    excess_caffeine = max(0, total_caffeine - DAILY_LIMIT)

    # Display the excess caffeine consumption
    result = excess_caffeine
    return result

print(solution())