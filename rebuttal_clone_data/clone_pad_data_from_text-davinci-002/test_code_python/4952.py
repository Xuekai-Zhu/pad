def solution():
    cost_adult = 7
    cost_child = 3
    total_cost = 6000
    total_people = total_cost / (cost_adult + cost_child)
    adults = total_people / 4
    children = total_people - adults
    result = adults, children
    
    return result

print(solution())