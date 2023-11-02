def solution():
    """Ben starts each day with $50, spends $15 every day and saves the rest. After a few days, his mom doubled his total savings and his dad gave him an additional $10. If he now has $500, How many days have elapsed?"""
    # Initialize variables
    starting_cash = 50
    daily_spending = 15
    total_savings = 0
    days_elapsed = 0

    # Calculate number of days
    while total_savings <= 235:
        total_savings += starting_cash - daily_spending
        days_elapsed += 1

    # Calculate new savings after mom's gift and dad's gift
    total_savings = (total_savings * 2) + 10

    # Check if total savings equal $500
    while total_savings < 500:
        days_elapsed += 1
        total_savings += starting_cash - daily_spending

    # Display number of days elapsed
    result = days_elapsed
    return result

print(solution())