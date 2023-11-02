def solution():
    
    hair_cost = 400
    manicure_cost = hair_cost / 4
    pedicure_cost = manicure_cost * 3 / 4
    total_cost = hair_cost + manicure_cost + pedicure_cost
    result = total_cost
    return result

print(solution())