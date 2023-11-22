def solution():
    
    # Define the cost of each candy of type A and B
    A_PRICE = 0.5
    B_PRICE = 0.75

    # Define the number of candies of type A and B purchased
    A_CANDYS = 7
    B_CANDYS = 10

    # Calculate the total cost of the type A and B purchased
    A_total_cost = A_CANDYS * A_PRICE
    B_total_cost = B_CANDYS * B_PRICE

    # Calculate the total cost of the purchase
    total_cost = A_total_cost + B_total_cost

    # Calculate the change Adam will receive
    change = 15 - total_cost

    # Display the change
    result = change
    return result

print(solution())