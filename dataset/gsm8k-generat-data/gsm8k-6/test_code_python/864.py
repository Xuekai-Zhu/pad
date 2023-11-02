def solution():
    # Calculate the total number of coffee cups brewed on the weekend
    weekend_coffee = 120 - (10*5*2)  # Subtract the coffee brewed on weekdays from the total weekend coffee

    # Calculate the total number of coffee cups brewed in 1 week
    weekly_coffee = (10*5*7) + weekend_coffee  # 10 coffee cups brewed per hour for 5 hours per day for 7 days in a week
    result = weekly_coffee
    return result

print(solution())