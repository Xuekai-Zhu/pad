def solution():
    tomato_price = 5
    apple_price = 6

    num_tomatoes = 2
    num_apples = 5

    # Calculate the total cost of tomatoes
    total_tomato_cost = num_tomatoes * tomato_price

    # Calculate the total cost of apples
    total_apple_cost = num_apples * apple_price

    # Calculate the total cost of all items
    total_cost = total_tomato_cost + total_apple_cost
    result = total_cost
    return result

print(solution())