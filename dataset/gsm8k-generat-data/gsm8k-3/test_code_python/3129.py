def solution():
    """Mike buys 6 rose bushes at 75 dollars each, 2 of them are for his friend and the rest are for him.  He also buys 2 tiger tooth aloes for 100 dollars each.  How much money did he spend on plants for himself?"""
    # Define the cost of each type of plant
    ROSE_PRICE = 75
    ALOE_PRICE = 100

    # Calculate the total cost of the rose bushes
    rose_cost = 6 * ROSE_PRICE

    # Calculate the cost of the rose bushes for his friend
    friend_cost = 2 * ROSE_PRICE

    # Calculate the cost of the rose bushes for Mike
    mike_cost = rose_cost - friend_cost

    # Calculate the total cost of the tiger tooth aloes
    aloe_cost = 2 * ALOE_PRICE

    # Calculate the total cost of the plants for Mike
    total_cost = mike_cost + aloe_cost

    # Display the total cost of the plants for Mike
    result = total_cost
    return result

print(solution())