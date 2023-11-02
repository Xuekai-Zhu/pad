def solution():
    coffee_weight = 3  # Angie bought 3 lbs. of coffee
    cups_per_lb = 40  # Each lb. of coffee will brew about 40 cups of coffee
    cups_per_day = 3  # Angie drinks 3 cups of coffee every day

    # Calculate the total number of cups of coffee from the purchased coffee
    total_cups = coffee_weight * cups_per_lb

    # Calculate the number of days the coffee will last Angie
    days = total_cups // cups_per_day

    result = days
    return result

print(solution())