def solution():
    """Rachel and Sara want to attend a beauty and modeling contest. They both want to buy new pairs of shoes and dresses. Sara buys a pair of shoes which costs $50 and a dress which costs $200. How much should Rachel budget if she wants to spend twice as much as what Sara spent on the pair of shoes and dress?"""
    cost_of_sara_shoes = 50
    cost_of_sara_dress = 200
    total_cost_of_sara = cost_of_sara_shoes + cost_of_sara_dress
    cost_of_rachel_shoes = 2 * cost_of_sara_shoes
    cost_of_rachel_dress = 2 * cost_of_sara_dress
    total_cost_of_rachel = cost_of_rachel_shoes + cost_of_rachel_dress
    result = total_cost_of_rachel
    
    return result

print(solution())