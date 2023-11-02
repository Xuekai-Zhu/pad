def solution():
    # Define the quantities and prices of the items
    apple_quantity = 5
    apple_price = 2
    sugar_quantity = 3
    sugar_price = apple_price - 1
    walnut_quantity = 0.5
    walnut_price = 6

    # Calculate the total cost of each item
    apple_cost = apple_quantity * apple_price
    sugar_cost = sugar_quantity * sugar_price
    walnut_cost = walnut_quantity * walnut_price

    # Calculate the total cost of all items
    total_cost = apple_cost + sugar_cost + walnut_cost
    result = total_cost
    return result

print(solution())