def solution():
    """Bob buys nose spray. He buys 10 of them for a "buy one get one free" promotion. They each cost $3. How much does he pay?"""
    # Define the cost per nose spray and the number purchased
    COST = 3
    NUM_SPRAYS = 10

    # Calculate the total cost, accounting for the "buy one get one free" promotion
    total_cost = (NUM_SPRAYS // 2 + NUM_SPRAYS % 2) * COST

    # Display the total cost
    result = total_cost
    return result

print(solution())