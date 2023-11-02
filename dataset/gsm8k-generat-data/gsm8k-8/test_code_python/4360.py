def solution():
    # Define the price of tea
    tea_price = 10

    # Calculate the price of cheese
    cheese_price = tea_price / 2

    # Calculate the price of butter
    butter_price = 0.8 * cheese_price

    # Calculate the price of bread
    bread_price = butter_price / 2

    # Calculate the total cost of all items
    total_cost = tea_price + cheese_price + butter_price + bread_price

    result = total_cost
    return result

print(solution())