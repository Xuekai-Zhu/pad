def solution():
    
    # Define the prices and quantities of each item
    apple_price = 4
    banana_price = 2
    orange_price = 3
    apple_quantity = 1
    banana_quantity = 2
    orange_quantity = 2

    # Calculate the total cost of each item
    apple_cost = apple_price * apple_quantity
    banana_cost = banana_price * banana_quantity
    orange_cost = orange_price * orange_quantity

    # Calculate the total cost of all items
    total_cost = apple_cost + banana_cost + orange_cost

    # return the result
    result = total_cost
    return result

print(solution())