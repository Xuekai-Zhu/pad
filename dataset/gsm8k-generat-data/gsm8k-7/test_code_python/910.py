def solution():
    jug_size = 0.5  # gallons
    days_per_jug = 4
    cups_per_gallon = 16

    # Calculate the total amount of coffee per day in cups
    total_coffee_per_day = jug_size * cups_per_gallon / days_per_jug
    result = total_coffee_per_day
    return result

print(solution())