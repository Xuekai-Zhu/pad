def solution():
    
    pack_cost = 10
    bagel_cost = pack_cost * 9
    num_packs = 4
    discount = 0.1
    total_cost = (pack_cost * num_packs) * (1 - discount)
    num_bags = 4
    cost_per_bagel = total_cost / num_bags
    result = cost_per_bagel
    return result

print(solution())