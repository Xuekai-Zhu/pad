def solution():
    """Jonah bought 6 pineapples for $3 each. Each pineapple could be cut into 12 pineapple rings. He sold 4 pineapple rings for $5 each. How much profit did Jonah make?"""
    # Define the cost and number of pineapples purchased
    COST_PER_PINEAPPLE = 3
    NUM_PINEAPPLES = 6

    # Calculate the total cost of the pineapples
    total_cost = COST_PER_PINEAPPLE * NUM_PINEAPPLES

    # Calculate the number of pineapple rings
    num_rings = NUM_PINEAPPLES * 12

    # Calculate the total revenue from selling pineapple rings
    total_revenue = (num_rings / 4) * 5

    # Calculate the profit
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())