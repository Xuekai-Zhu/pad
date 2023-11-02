def solution():
    # Define variables
    gallons_per_day = 1.5
    quarts_per_gallon = 4
    days_per_week = 7

    # Calculate the total quarts per week
    quarts_per_week = gallons_per_day * quarts_per_gallon * days_per_week
    result = quarts_per_week
    return result

print(solution())