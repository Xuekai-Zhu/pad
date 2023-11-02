def solution():
    # Use the formula: wages = (workers * days * rate)
    # Calculate the rate per worker per day
    rate = 9450 / (15*6)  

    # Calculate the wages for 19 workers for 5 days
    wages = 19 * 5 * rate
    result = wages
    return result

print(solution())