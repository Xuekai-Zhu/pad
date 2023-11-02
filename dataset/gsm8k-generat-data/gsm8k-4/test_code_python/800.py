def solution():
    """Cappuccinos cost $2, iced teas cost $3, cafe lattes cost $1.5 and espressos cost $1 each. Sandy orders some drinks for herself and some friends. She orders three cappuccinos, two iced teas, two cafe lattes, and two espressos. How much change does she receive back for a twenty-dollar bill?"""
    # Define the prices of each drink
    cappuccino_price = 2
    iced_tea_price = 3
    cafe_latte_price = 1.5
    espresso_price = 1

    # Calculate the total cost of Sandy's order
    total_cost = (3 * cappuccino_price) + (2 * iced_tea_price) + (2 * cafe_latte_price) + (2 * espresso_price)

    # Calculate the change from a twenty-dollar bill
    change = 20 - total_cost

    # return the result
    result = change
    return result

print(solution())