def solution():
    """Martha buys 1 latte for $4.00 every morning, 5 days a week.  3 days a week, she buys an iced coffee for $2.00.  Her goal for the entire year is to cut her coffee spending by 25%.  How much will she save?"""
    # Define the price of a latte and the price of an iced coffee
    LATTE_PRICE = 4
    ICED_COFFEE_PRICE = 2

    # Calculate the total spent on lattes per week, and per year
    lattes_per_week = 5
    lattes_per_year = lattes_per_week * 52
    lattes_spent_per_year = lattes_per_year * LATTE_PRICE

    # Calculate the total spent on iced coffees per week, and per year
    iced_coffees_per_week = 3
    iced_coffees_per_year = iced_coffees_per_week * 52
    iced_coffees_spent_per_year = iced_coffees_per_year * ICED_COFFEE_PRICE

    # Calculate the total spent on coffee per year
    total_spent_per_year = lattes_spent_per_year + iced_coffees_spent_per_year

    # Calculate the amount to be saved, and the new total spending after cutting by 25%
    amount_saved = total_spent_per_year * 0.25
    new_total_spending = total_spent_per_year - amount_saved

    # Return the amount saved
    result = amount_saved
    return result

print(solution())