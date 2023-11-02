def solution():
    """Rihanna has $50 to go to the supermarket. Rihanna bought 6 mangoes and 6 cartons of apple juice. Each mango cost $3 and each carton of apple juice cost $3. How much money does Rihanna have left?"""
    # Define the prices and quantities of mangoes and apple juice
    mango_price = 3
    mango_quantity = 6
    juice_price = 3
    juice_quantity = 6

    # Calculate the total cost of mangoes and apple juice
    mango_cost = mango_price * mango_quantity
    juice_cost = juice_price * juice_quantity
    total_cost = mango_cost + juice_cost

    # Calculate the amount of money Rihanna has left
    remaining_money = 50 - total_cost
    result = remaining_money
    return result

print(solution())