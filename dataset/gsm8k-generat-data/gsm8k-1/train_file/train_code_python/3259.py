def solution():
    """Martha buys 1 latte for $4.00 every morning, 5 days a week. 3 days a week, she buys an iced coffee for $2.00. Her goal for the entire year is to cut her coffee spending by 25%. How much will she save?"""
    latte_price = 4.00
    iced_coffee_price = 2.00
    days_per_week = 5
    lattes_per_week = days_per_week
    iced_coffees_per_week = 3
    lattes_per_year = lattes_per_week * 52
    iced_coffees_per_year = iced_coffees_per_week * 52
    initial_spending = (lattes_per_year * latte_price) + (iced_coffees_per_year * iced_coffee_price)
    savings_goal_percent = 25/100
    savings = initial_spending * savings_goal_percent
    result = savings
    return result

print(solution())