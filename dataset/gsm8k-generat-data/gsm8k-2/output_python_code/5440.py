def solution():
    """Mustafa buys a fridge, a TV, and a computer with a total budget of $1600. The TV costs $600, and the fridge costs $500 more than the computer. How much does the computer cost?"""
    total_budget = 1600
    tv_cost = 600
    fridge_cost = 500 + computer_cost
    computer_cost = (total_budget - tv_cost - fridge_cost)
    result = computer_cost
    return result

print(solution())