def solution():
    """Jonah bought 6 pineapples for $3 each. Each pineapple could be cut into 12 pineapple rings. He sold 4 pineapple rings for $5 each. How much profit did Jonah make?"""
    # Define the cost of each pineapple
    pineapple_cost = 3

    # Define the number of pineapples
    num_pineapples = 6

    # Calculate the total cost of the pineapples
    total_cost = pineapple_cost * num_pineapples

    # Calculate the number of pineapple rings
    num_rings = num_pineapples * 12

    # Calculate the total revenue from selling pineapple rings
    total_revenue = (num_rings // 4) * 5

    # Calculate the profit
    profit = total_revenue - total_cost

    # Return the result
    result = profit
    return result

print(solution())