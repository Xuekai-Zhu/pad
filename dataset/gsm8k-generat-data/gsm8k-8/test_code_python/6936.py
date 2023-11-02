def solution():
    # Define the prices and quantities of each type of produce
    asparagus_price = 3.00
    asparagus_quantity = 60
    grapes_price = 2.50
    grapes_quantity = 40
    apples_price = 0.50
    apples_quantity = 700

    # Calculate the total cost of each type of produce
    asparagus_cost = asparagus_price * asparagus_quantity
    grapes_cost = grapes_price * grapes_quantity
    apples_cost = apples_price * apples_quantity

    # Calculate the total cost of all the produce
    total_cost = asparagus_cost + grapes_cost + apples_cost
    result = total_cost
    return result

print(solution())