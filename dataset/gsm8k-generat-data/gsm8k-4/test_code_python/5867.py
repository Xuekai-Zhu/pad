def solution():
    """Sophie's aunt gave her $260 to spend on clothes at the mall. She bought 2 shirts that cost $18.50 each and a pair of trousers that cost $63. She then decides to purchase 4 more articles of clothing with her remaining budget. How much money would each item cost if she split the cost of each item evenly?"""
    # Define the initial budget and the cost of the first purchases
    initial_budget = 260
    shirt_cost = 18.5
    trousers_cost = 63

    # Calculate the cost of the first purchases
    total_cost = (2 * shirt_cost) + trousers_cost

    # Calculate the remaining budget
    remaining_budget = initial_budget - total_cost

    # Calculate the cost of each of the additional purchases
    each_cost = remaining_budget / 4

    # Display the cost of each item
    result = each_cost
    return result

print(solution())