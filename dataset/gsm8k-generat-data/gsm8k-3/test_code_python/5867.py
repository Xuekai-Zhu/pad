def solution():
    """Sophie's aunt gave her $260 to spend on clothes at the mall. She bought 2 shirts that cost $18.50 each and a pair of trousers that cost $63. She then decides to purchase 4 more articles of clothing with her remaining budget. How much money would each item cost if she split the cost of each item evenly?"""
    # Define the cost of each item of clothing
    shirt_cost = 18.5
    trouser_cost = 63

    # Calculate the total cost of the first three items
    total_cost = (2 * shirt_cost) + trouser_cost

    # Calculate the remaining budget
    remaining_budget = 260 - total_cost

    # Calculate the cost per item for the remaining four items
    cost_per_item = remaining_budget / 4

    # Display the cost per item
    result = cost_per_item
    return result

print(solution())