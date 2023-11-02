def solution():
    latte_price = 4.0
    iced_coffee_price = 2.0
    num_latte_per_week = 5
    num_iced_coffee_per_week = 3
    num_weeks_per_year = 52

    # Calculate the total cost of all lattes for the year
    total_latte_cost = latte_price * num_latte_per_week * num_weeks_per_year

    # Calculate the total cost of all iced coffees for the year
    total_iced_coffee_cost = iced_coffee_price * num_iced_coffee_per_week * num_weeks_per_year

    # Calculate the total cost of all coffee for the year
    total_coffee_cost = total_latte_cost + total_iced_coffee_cost

    # Calculate the new total cost after the 25% discount
    new_total_cost = total_coffee_cost * 0.75

    # Calculate the savings
    savings = total_coffee_cost - new_total_cost
    result = savings
    return result

print(solution())