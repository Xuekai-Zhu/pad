def solution():
    adult_ticket = 50 / 2
    kid_ticket = adult_ticket / 2
    total_cost = 50
    num_kids = 6
    num_adults = 2
    cost_per_kid = total_cost - (adult_ticket * num_adults)
    result = cost_per_kid / num_kids
    
    return result

print(solution())