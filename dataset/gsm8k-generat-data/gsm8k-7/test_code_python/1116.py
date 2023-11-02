def solution():
    daily_spending = 15
    starting_amount = 50

    # Calculate the number of days before doubling savings and adding $10
    days_elapsed = (500 - 10) / (starting_amount - daily_spending * 2)

    result = days_elapsed
    return result

print(solution())