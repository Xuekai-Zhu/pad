def solution():
    
    total_promised = 400
    total_received = 285
    remaining_amount = total_promised - total_received
    amy_owes = 30
    derek_owes = amy_owes / 2
    sally_carl_owes = remaining_amount - amy_owes - derek_owes
    individual_owes = sally_carl_owes / 2
    result = individual_owes
    return result

print(solution())