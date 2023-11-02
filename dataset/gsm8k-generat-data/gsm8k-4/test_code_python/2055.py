def solution():
    """Sarah makes 5 times more money per hour than Connor does. If Connor earns $7.20 per hour, how much does Sarah make in an 8-hour day?"""
    # Define Connor's hourly wage
    connor_wage = 7.20

    # Calculate Sarah's hourly wage
    sarah_wage = 5 * connor_wage

    # Calculate Sarah's daily earnings
    sarah_day_earnings = sarah_wage * 8

    # Return Sarah's daily earnings
    result = sarah_day_earnings
    return result

print(solution())