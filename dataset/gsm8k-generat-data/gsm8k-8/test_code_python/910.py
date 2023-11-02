def solution():
    # Define the amount of coffee purchased and days between purchases
    coffee_purchase = 1/2
    days_between_purchases = 4

    # Calculate the amount of coffee consumed per day
    coffee_consumed_per_day = coffee_purchase / days_between_purchases * 16
    # Convert from gallons to cups and round to the nearest whole number
    result = round(coffee_consumed_per_day)
    return result

print(solution())