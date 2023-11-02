def solution():
    """Mustafa buys a fridge, a TV and a computer with a total budget of $1600. The TV costs $600 and the fridge costs $500 more than the computer. How much does the computer cost?"""
    # Define the cost of the TV and the total budget
    tv_cost = 600
    total_budget = 1600

    # Calculate the remaining budget after purchasing the TV
    remaining_budget = total_budget - tv_cost

    # Calculate the maximum cost of the fridge
    max_fridge_cost = remaining_budget - 500

    # Calculate the cost of the computer as the remaining budget
    computer_cost = remaining_budget - max_fridge_cost

    result = computer_cost
    return result

print(solution())