def solution():
    """Martha buys 1 latte for $4.00 every morning, 5 days a week.  3 days a week, she buys an iced coffee for $2.00.  Her goal for the entire year is to cut her coffee spending by 25%.  How much will she save?"""
    # Define the cost of a latte and an iced coffee
    LATTE_COST = 4.00
    ICED_COFFEE_COST = 2.00

    # Calculate the cost of lattes per week and per year
    weekly_latte_cost = 5 * LATTE_COST
    yearly_latte_cost = weekly_latte_cost * 52

    # Calculate the cost of iced coffees per week and per year
    weekly_iced_coffee_cost = 3 * ICED_COFFEE_COST
    yearly_iced_coffee_cost = weekly_iced_coffee_cost * 52

    # Calculate the total yearly coffee spending
    total_spending = yearly_latte_cost + yearly_iced_coffee_cost

    # Calculate the 25% reduction in coffee spending
    reduced_spending = total_spending * 0.25

    # Display the amount saved
    result = reduced_spending
    return result

print(solution())