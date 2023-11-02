def solution():
    caffeine_per_cup = 80  # There is 80 mg of caffeine in a cup of coffee
    max_caffeine_per_day = 200  # Lisa does not want to drink more than 200 mg of caffeine per day
    cups_of_coffee = 3  # Lisa drinks three cups of coffee

    # Calculate the total amount of caffeine in the coffee Lisa drinks
    total_caffeine = caffeine_per_cup * cups_of_coffee

    # Calculate how many milligrams of caffeine Lisa drank over her goal
    over_goal = max(0, total_caffeine - max_caffeine_per_day)
    result = over_goal
    return result

print(solution())