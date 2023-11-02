def solution():
    """Martha buys 1 latte for $4.00 every morning, 5 days a week. 3 days a week, she buys an iced coffee for $2.00. Her goal for the entire year is to cut her coffee spending by 25%. How much will she save?"""
    weekly_latte_cost = 4 * 5
    weekly_iced_coffee_cost = 2 * 3
    yearly_latte_cost = weekly_latte_cost * 52
    yearly_iced_coffee_cost = weekly_iced_coffee_cost * 52
    total_spending = yearly_latte_cost + yearly_iced_coffee_cost
    savings = total_spending * 0.25
    result = savings
    return result

print(solution())