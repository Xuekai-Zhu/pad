def solution():
    pastry_price = 5  # Pastries are sold for $5 each
    days_per_week = 7  # The baker works 7 days per week

    # Calculate the total number of pastries sold in a week
    total_pastries = 2 + sum(range(1, 7))  # The baker sold 2 pastries on Monday and the number increases by 1 every day

    # Calculate the average number of pastries sold per day
    average_pastries_per_day = total_pastries / days_per_week
    result = average_pastries_per_day
    return result

print(solution())