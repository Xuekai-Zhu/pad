def solution():
    """Jan buys 5 dozen roses. Each rose cost $6. Since he bought so many he only needs to pay 80%. How much did he pay?"""
    # Define the number of roses and the price of one rose
    roses = 5 * 12
    price = 6.0

    # Calculate the total cost before the discount
    total_cost = roses * price

    # Apply the discount
    discounted_cost = total_cost * 0.8

    # Return the final cost
    result = discounted_cost
    return result

print(solution())