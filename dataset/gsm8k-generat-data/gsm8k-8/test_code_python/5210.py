def solution():
    # Define the amount of caffeine in one cup of coffee
    caffeine_per_cup = 80

    # Define the maximum amount of caffeine Lisa wants to drink in one day
    max_caffeine_per_day = 200

    # Calculate the maximum number of cups of coffee Lisa can drink in one day
    max_cups_per_day = max_caffeine_per_day / caffeine_per_cup

    # Define the number of cups of coffee Lisa drinks
    num_cups = 3

    # Calculate the total amount of caffeine Lisa drinks
    total_caffeine = num_cups * caffeine_per_cup

    # Calculate the amount of caffeine Lisa drinks over her goal
    over_goal = total_caffeine - max_caffeine_per_day

    result = over_goal
    return result

print(solution())