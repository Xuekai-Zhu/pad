def solution():
    """Ben starts each day with $50, spends $15 every day and saves the rest. After a few days, his mom doubled his total savings and his dad gave him an additional $10. If he now has $500, How many days have elapsed?"""
    # Define the initial amount of money, daily spending, and the number of days elapsed
    initial_money = 50
    daily_spending = 15
    days_elapsed = 0

    # Define the total savings and the total amount of money earned from parents
    total_savings = 0
    total_earned = 0

    # Calculate the savings and the total amount earned each day, until the total amount reaches $500
    while total_savings + initial_money + total_earned + 10 < 500:
        # Increment the day counter
        days_elapsed += 1

        # Calculate the amount saved each day
        daily_savings = initial_money - daily_spending

        # Add the daily savings to the total savings
        total_savings += daily_savings

        # Double the total savings if the number of days elapsed is even
        if days_elapsed % 2 == 0:
            total_savings *= 2

        # Add $10 to the total amount earned
        total_earned += 10

    result = days_elapsed
    return result

print(solution())