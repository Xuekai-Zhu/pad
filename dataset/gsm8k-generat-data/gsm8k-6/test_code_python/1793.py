def solution():
    # Calculate the amount of money Dawn makes per painting
    payment_per_painting = 3600 / 12

    # Calculate the time it takes to paint one painting
    time_per_painting = 2

    # Calculate the amount of money Dawn makes per hour
    payment_per_hour = payment_per_painting / time_per_painting
    result = payment_per_hour
    return result

print(solution())