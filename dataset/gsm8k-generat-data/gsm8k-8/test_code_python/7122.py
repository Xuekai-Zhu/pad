def solution():
    # Define the price and weight of the tomatoes and apples
    tomato_price = 5
    tomato_weight = 2
    apple_price = 6
    apple_weight = 5

    # Calculate the total cost of the tomatoes and apples
    tomato_cost = tomato_price * tomato_weight
    apple_cost = apple_price * apple_weight

    # Calculate the total cost of Mark's purchase
    total_cost = tomato_cost + apple_cost
    result = total_cost
    return result

print(solution())