def solution():
    # Calculate Martha's total spending on coffee for a week
    weekly_spending = (1 * 4 * 5) + (3 * 2)  # 1 latte for $4.00 every morning for 5 days, and 3 iced coffees for $2.00 each
    yearly_spending = weekly_spending * 52  # total spending for a year

    # Calculate how much Martha wants to save
    savings_goal = yearly_spending * 0.25

    result = savings_goal
    return result

print(solution())