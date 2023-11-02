def solution():
    num_apples = 4
    apple_price = 5.20

    num_oranges = 3
    orange_price = 3.30

    # Calculate the total cost of 5 apples
    total_apple_cost = num_apples * apple_price

    # Calculate the total cost of 5 oranges
    total_orange_cost = num_oranges * orange_price

    # Calculate the total cost of 5 apples and 5 oranges
    total_cost = total_apple_cost + total_orange_cost
    result = total_cost
    return result

print(solution())