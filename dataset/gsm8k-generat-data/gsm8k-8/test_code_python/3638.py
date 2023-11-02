def solution():
    # Define the prices and number of items sold
    pizza_price = 12
    fries_price = 0.3
    soda_price = 2
    num_pizzas_sold = 15
    num_fries_sold = 40
    num_sodas_sold = 25

    # Calculate the total money raised
    total_money_raised = (pizza_price * num_pizzas_sold) + (fries_price * num_fries_sold) + (soda_price * num_sodas_sold)

    # Calculate the difference between the total money raised and the goal
    difference = 500 - total_money_raised
    result = difference
    return result

print(solution())