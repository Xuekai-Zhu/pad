def solution():
    hours_worked = 8  # Ian worked 8 hours doing surveys
    earnings_per_hour = 18  # Ian earns $18 per hour doing surveys
    total_earnings = hours_worked * earnings_per_hour  # Ian earned a total of $144
    money_spent = total_earnings / 2  # Ian spent half of his total earnings
    money_left = total_earnings - money_spent  # Calculate how much money Ian has left
    result = money_left
    return result

print(solution())