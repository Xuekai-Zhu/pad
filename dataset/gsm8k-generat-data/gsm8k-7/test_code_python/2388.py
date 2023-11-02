def solution():
    apple_price_per_dozen = 40
    pear_price_per_dozen = 50
    num_dozen_apples = 14
    num_dozen_pears = 14

    # Calculate the total cost of all apples
    total_apple_cost = apple_price_per_dozen * num_dozen_apples

    # Calculate the total cost of all pears
    total_pear_cost = pear_price_per_dozen * num_dozen_pears

    # Calculate the total cost of all fruits
    total_cost = total_apple_cost + total_pear_cost
    result = total_cost
    return result

print(solution())