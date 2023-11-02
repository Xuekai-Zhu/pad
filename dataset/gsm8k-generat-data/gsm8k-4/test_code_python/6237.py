def solution():
    """Brendan makes $6/hour as a waiter. He's scheduled for 2 8-hour shifts and 1 12-hour shift this week. He also makes an average of $12 in tips each hour. Brendan is supposed to pay 20% of his income in taxes, but he only reports 1/3rd of his tips to the IRS. How much money does Brendan pay in taxes each week?"""
    # Define Brendan's hourly wage, hours worked, and tips earned
    hourly_wage = 6
    hours_worked = [8, 8, 12]
    tips_per_hour = 12

    # Calculate Brendan's income before taxes
    income = sum(hours_worked) * hourly_wage + tips_per_hour * sum(hours_worked)

    # Calculate Brendan's taxes owed (assuming he reports all of his tips)
    taxes = income * 0.2

    # Calculate Brendan's unreported tips
    unreported_tips = (tips_per_hour * sum(hours_worked)) / 3

    # Recalculate Brendan's taxes owed with only reported tips
    taxes_reported_tips = (income - unreported_tips) * 0.2

    # Choose the lower of the two tax amounts
    taxes_owed = min(taxes, taxes_reported_tips)

    result = taxes_owed
    return result

print(solution())