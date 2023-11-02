def solution():
    """Woody wants to buy a games console that costs $282. Woody already has $42 and receives an allowance of $24 every week. How many weeks will it take him to save the money he needs for the game console?"""
    console_price = 282
    current_savings = 42
    weekly_allowance = 24
    weeks_needed = (console_price - current_savings) / weekly_allowance
    result = weeks_needed
    return result

print(solution())