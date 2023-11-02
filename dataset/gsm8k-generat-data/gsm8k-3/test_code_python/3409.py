def solution():
    """Peter needs 80 ounces of soda for his party. He sees that 8 oz cans cost $.5 each. How much does he spend on soda if he buys the exact number of cans he needs?"""
    # Define the size of each can of soda and its cost
    CAN_SIZE = 8
    CAN_COST = 0.5

    # Calculate the number of cans Peter needs to buy
    num_cans = 80 / CAN_SIZE

    # Calculate the total cost of the cans of soda
    total_cost = num_cans * CAN_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())