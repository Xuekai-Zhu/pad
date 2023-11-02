def solution():
    # Define the prices of each drink
    cappuccino_price = 2
    iced_tea_price = 3
    cafe_latte_price = 1.5
    espresso_price = 1

    # Calculate the total cost of Sandy's order
    total_cost = 3*cappuccino_price + 2*iced_tea_price + 2*cafe_latte_price + 2*espresso_price

    # Calculate the change from a twenty-dollar bill
    change = 20 - total_cost
    result = change
    return result

print(solution())