def solution():
    
    cuff_length = 50
    hem_length = 300
    waist_length = hem_length / 3
    ruffle_length = 5 * 20
    total_length = cuff_length * 2 + hem_length + waist_length + ruffle_length
    cost_per_meter = 6
    total_cost = total_length / 100 * cost_per_meter
    
    return total_cost

print(solution())