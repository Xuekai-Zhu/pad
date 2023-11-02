def solution():
    robert_pizza_boxes = 5
    robert_pizza_box_price = 10
    robert_drinks = 10
    robert_drink_price = 2

    teddy_hamburgers = 6
    teddy_hamburger_price = 3
    teddy_drinks = 10

    # Calculate the cost of Robert's pizza and drinks
    robert_pizza_cost = robert_pizza_boxes * robert_pizza_box_price
    robert_drink_cost = robert_drinks * robert_drink_price

    # Calculate the cost of Teddy's hamburgers and drinks
    teddy_hamburger_cost = teddy_hamburgers * teddy_hamburger_price
    teddy_drink_cost = robert_drinks * robert_drink_price

    # Calculate the total cost of all snacks
    total_cost = robert_pizza_cost + robert_drink_cost + teddy_hamburger_cost + teddy_drink_cost
    result = total_cost
    return result

print(solution())