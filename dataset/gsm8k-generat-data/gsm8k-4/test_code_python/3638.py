def solution():
    """To support the school outreach program, Einstein wants to raise $500 by selling snacks. One box of pizza sells for $12, a pack of potato fries sells for $0.30, and a can of soda at $2. Einstein sold 15 boxes of pizzas, 40 packs of potato fries, and 25 cans of soda. How much more money does Einstein need to raise to reach his goal?"""
    # Define the prices and quantities of snacks sold
    pizza_price = 12
    pizza_quantity = 15
    fries_price = 0.3
    fries_quantity = 40
    soda_price = 2
    soda_quantity = 25

    # Calculate the total sales
    total_sales = (pizza_price * pizza_quantity) + \
                  (fries_price * fries_quantity) + \
                  (soda_price * soda_quantity)

    # Calculate the difference between the total sales and the goal amount
    difference = 500 - total_sales

    # Round the difference to 2 decimal places
    result = round(difference, 2)
    return result

print(solution())