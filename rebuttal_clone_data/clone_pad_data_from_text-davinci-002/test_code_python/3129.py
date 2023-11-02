def solution():
    rose_bushes = 6
    tiger_tooth_aloes = 2
    rose_bushes_bought_for_friend = 2
    rose_bushes_bought_for_self = rose_bushes - rose_bushes_bought_for_friend
    cost_of_rose_bushes = rose_bushes * 75
    cost_of_tiger_tooth_aloes = tiger_tooth_aloes * 100
    total_cost = cost_of_rose_bushes + cost_of_tiger_tooth_aloes
    cost_of_plants_for_self = total_cost - (rose_bushes_bought_for_friend * 75)
    result = cost_of_plants_for_self
    
    return result

print(solution())