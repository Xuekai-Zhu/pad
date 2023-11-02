def solution():
    # Calculate Martha's total weekly spending on lattes
    lattes_weekly = 1 * 4 * 5
    # Calculate Martha's total weekly spending on iced coffee
    iced_coffee_weekly = 3 * 2 * 5
    # Calculate Martha's total weekly spending before her goal to cut spending by 25%
    weekly_spending_before_goal = lattes_weekly + iced_coffee_weekly
    # Calculate Martha's total weekly spending after her goal to cut spending by 25%
    weekly_spending_after_goal = weekly_spending_before_goal * 0.75
    # Calculate the weekly savings
    weekly_savings = weekly_spending_before_goal - weekly_spending_after_goal
    # Calculate the total savings for the year
    yearly_savings = weekly_savings * 52
    result = yearly_savings
    return result

print(solution())