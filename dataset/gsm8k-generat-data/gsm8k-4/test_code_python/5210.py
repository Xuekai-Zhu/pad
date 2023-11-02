def solution():
    """There is 80 mg of caffeine in a cup of coffee. Lisa does not want to drink more than 200 mg of caffeine per day. If she drinks three cups of coffee, how many milligrams of coffee did Lisa drink over her goal?"""
    # Define the maximum amount of caffeine Lisa wants to drink
    MAX_CAFFEINE = 200

    # Define the amount of caffeine in a cup of coffee
    COFFEE_CAFFEINE = 80

    # Calculate the total amount of caffeine Lisa drank from three cups of coffee
    total_caffeine = COFFEE_CAFFEINE * 3

    # Calculate the amount of caffeine Lisa drank over her goal
    over_goal = max(0, total_caffeine - MAX_CAFFEINE)

    # Return the result
    result = over_goal
    return result

print(solution())