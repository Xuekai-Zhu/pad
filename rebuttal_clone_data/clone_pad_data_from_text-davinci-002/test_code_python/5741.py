def solution():
    hair_cost = 50
    nails_cost = 30
    tip = 20
    total_cost = (hair_cost + nails_cost) + ((hair_cost + nails_cost) * (tip / 100))
    result = total_cost
    return result

print(solution())