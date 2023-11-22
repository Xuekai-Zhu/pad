def solution():
    
    # Define the original price of the jeans
    original_price = 40

    # Calculate the discounted price of the jeans
    discounted_price = original_price * 0.75

    # Calculate the total cost of the jeans
    total_cost = discounted_price * 2

    # Calculate the amount of money Mike will have left over
    leftover_money = 50 - total_cost

    # Display the amount of money Mike will have left over
    result = leftover_money
    return result

print(solution())