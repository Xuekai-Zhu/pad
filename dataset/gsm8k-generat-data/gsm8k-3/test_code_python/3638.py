def solution():
    """To support the school outreach program, Einstein wants to raise $500 by selling snacks. One box of pizza sells for $12, a pack of potato fries sells for $0.30, and a can of soda at $2. Einstein sold 15 boxes of pizzas, 40 packs of potato fries, and 25 cans of soda. How much more money does Einstein need to raise to reach his goal?"""
    # Define the prices of the snacks
    PIZZA_PRICE = 12
    FRIES_PRICE = 0.3
    SODA_PRICE = 2

    # Define the quantities of each snack sold
    pizza_qty = 15
    fries_qty = 40
    soda_qty = 25

    # Calculate the total revenue from snack sales
    pizza_sales = pizza_qty * PIZZA_PRICE
    fries_sales = fries_qty * FRIES_PRICE
    soda_sales = soda_qty * SODA_PRICE
    total_sales = pizza_sales + fries_sales + soda_sales

    # Calculate the remaining amount needed to reach the goal
    remaining_amount = 500 - total_sales

    # Display the remaining amount needed
    result = remaining_amount
    return result

print(solution())