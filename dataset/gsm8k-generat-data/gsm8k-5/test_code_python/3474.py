def solution():
    payment_per_weed = 0.05  # Heather gets paid 5 cents per weed
    payment_per_hour = 10.0  # Heather wants to earn $10 per hour
    seconds_per_hour = 60 * 60  # There are 60 minutes and 60 seconds in an hour

    # Calculate how many weeds Heather needs to pick in an hour to earn her desired payment
    weeds_per_hour = payment_per_hour / payment_per_weed

    # Calculate how many seconds Heather can take to pick a weed
    seconds_per_weed = seconds_per_hour / weeds_per_hour
    result = seconds_per_weed
    return result

print(solution())