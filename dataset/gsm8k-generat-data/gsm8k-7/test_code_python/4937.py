def solution():
    pear_price = 90
    orange_price = pear_price + banana_price
    banana_price = (pear_price - orange_price) * -1
    total_op_cost = 120
    total_op = 1  # number of oranges plus number of pears

    # Calculate the number of oranges and pears
    num_oranges = total_op_cost / (orange_price + pear_price)
    num_pears = total_op - num_oranges

    # Calculate the total price of all bananas
    num_bananas = 200
    banana_cost = num_bananas * banana_price

    # Calculate the total price of all oranges
    orange_cost = num_bananas * 2 * orange_price

    # Calculate the total cost
    total_cost = banana_cost + orange_cost
    result = total_cost
    return result

print(solution())