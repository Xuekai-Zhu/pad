def solution():
    
    mary_cost = 20 + 2
    elle_cost = andrea_cost = (4 * 1.5 + 10) / 2
    joe_cost = 5
    total_cost = mary_cost + elle_cost + andrea_cost + joe_cost
    cost_without_mary = total_cost - mary_cost
    difference = mary_cost - cost_without_mary
    result = difference
    return result

print(solution())