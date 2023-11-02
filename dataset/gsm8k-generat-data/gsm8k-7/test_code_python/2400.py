def solution():
    num_apples = 5
    apple_price = 1

    num_oranges = 2
    orange_price = 2

    # Calculate the total cost of apples
    total_apple_cost = num_apples * apple_price

    # Calculate the total cost of oranges
    total_orange_cost = num_oranges * orange_price

    # Calculate the total cost of all items
    total_cost = total_apple_cost + total_orange_cost
    result = total_cost
    return result

print(solution())