def solution():
    """Nine adults went to a play with seven children. Adult tickets are $11 each and children's tickets are $7 each. How many dollars more did the adults' tickets cost in total than the children's tickets in total?"""
    adult_tickets = 9
    adult_price = 11
    child_tickets = 7
    child_price = 7
    adult_total = adult_tickets * adult_price
    child_total = child_tickets * child_price
    difference = adult_total - child_total
    result = difference
    return result

print(solution())