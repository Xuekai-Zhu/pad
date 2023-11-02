def solution():
    
    permit_cost = 250
    contractor_cost = 150 * 5 * 3
    inspector_cost = 0.2 * contractor_cost
    total_cost = permit_cost + contractor_cost + inspector_cost
    result = total_cost
    return result

print(solution())