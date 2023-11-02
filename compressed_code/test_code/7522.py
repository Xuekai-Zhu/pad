def solution():
    
    num_people = 6
    ticket_cost = 50
    entree_cost = 10
    drink_cost = 30
    num_drinkers = num_people // 2

    total_cost = num_people * (ticket_cost + entree_cost) + num_drinkers * drink_cost
    refund = total_cost * 0.9
    loss = total_cost - refund
    result = loss
    
    return result

print(solution())