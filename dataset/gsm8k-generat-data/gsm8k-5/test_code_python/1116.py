def solution():
    starting_amount = 50  # Ben starts with $50 each day
    daily_spending = 15  # Ben spends $15 each day
    total_savings = 0  # Ben's initial savings is $0
    days_elapsed = 0  # Keep track of the number of days elapsed

    while total_savings < 245:  # Stop once Ben has saved $245
        total_savings += starting_amount - daily_spending  # Calculate Ben's savings for the day
        days_elapsed += 1  # Increment the number of days elapsed

    # After a few days, his mom doubled his total savings and his dad gave him an additional $10.
    total_savings *= 2
    total_savings += 10

    # Check if Ben now has $500 and calculate the number of days elapsed.
    while total_savings < 500:
        total_savings += starting_amount - daily_spending  # Calculate Ben's savings for the day
        days_elapsed += 1  # Increment the number of days elapsed

    result = days_elapsed
    return result

print(solution())