def solution():
    """Marisa gets $5 as pocket money every day from her parents. She buys 4 lollipops worth 25 cents each every day and saves the change in her piggy bank. How much money does she put in her piggy bank if she saves for 5 days?"""
    daily_spending = 4 * 0.25
    daily_savings = 5 - daily_spending
    total_savings = daily_savings * 5
    result = total_savings
    return result

print(solution())