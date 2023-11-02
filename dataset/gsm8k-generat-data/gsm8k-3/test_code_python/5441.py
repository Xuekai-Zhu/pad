def solution():
    """Mustafa buys a fridge, a TV and a computer with a total budget of $1600. The TV costs $600 and the fridge costs $500 more than the computer. How much does the computer cost?"""
    # Define the cost of the TV and the total budget
    TV_COST = 600
    TOTAL_BUDGET = 1600

    # Calculate the maximum cost of the fridge
    max_fridge_cost = TOTAL_BUDGET - TV_COST

    # Calculate the minimum cost of the computer
    min_computer_cost = (max_fridge_cost - 500) / 2

    # Display the cost of the computer
    result = min_computer_cost
    return result

print(solution())