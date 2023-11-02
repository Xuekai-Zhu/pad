def solution():
    """Nine adults went to a play with seven children. Adult tickets are $11 each and children's tickets are $7 each. How many dollars more did the adults' tickets cost in total than the children's tickets in total?"""
    adult_tickets = 9
    child_tickets = 7
    adult_price = 11
    child_price = 7
    adult_cost = adult_tickets * adult_price
    child_cost = child_tickets * child_price
    cost_difference = adult_cost - child_cost
    result = cost_difference
    return result

print(solution())