def solution():
    """Leila went to the supermarket to get some groceries. Then she headed to her mechanic to get her automobile fixed. If fixing her automobile cost $350 which was $50 more than thrice the amount she spent at the supermarket, how much has she spent altogether?"""
    
    mechanic_cost = 350
    supermarket_cost = (mechanic_cost - 50) / 3
    total_cost = mechanic_cost + supermarket_cost
    result = total_cost
    return result

print(solution())