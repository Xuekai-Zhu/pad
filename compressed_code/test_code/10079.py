def solution():
    
    sets_of_drill_bits = 5
    cost_per_set = 6
    pre_tax_total = sets_of_drill_bits * cost_per_set
    tax_rate = 0.10
    tax_amount = pre_tax_total * tax_rate
    total_cost = pre_tax_total + tax_amount
    result = total_cost
    return result

print(solution())