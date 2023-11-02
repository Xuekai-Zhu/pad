def solution():
    # Initialize variables
    starting_money = 50
    daily_spending = 15
    total_savings = 0
    days_elapsed = 0

    # Calculate Ben's savings each day and total savings
    while total_savings < 245:
        total_savings += starting_money - daily_spending
        starting_money -= daily_spending
        days_elapsed += 1

    # Calculate the number of days that have elapsed
    days_elapsed = ((500 - 245) / (total_savings * 2)) + days_elapsed + 1

    # Add the $10 from Ben's dad
    days_elapsed += 1

    result = days_elapsed
    return result

print(solution())