def solution():
    
    num_shirts = 4
    num_pants = 2
    num_jackets = 2
    shirt_cost = 8
    pant_cost = 18
    jacket_cost = 60
    total_cost = (num_shirts * shirt_cost) + (num_pants * pant_cost) + (num_jackets * jacket_cost)
    carrie_share = total_cost / 2
    result = carrie_share
    return result

print(solution())