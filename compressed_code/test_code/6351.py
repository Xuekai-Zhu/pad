def solution():
    
    samosas = 3
    samosa_cost = 2
    pakoras = 4
    pakora_cost = 3
    lassi_cost = 2
    sub_total = (samosas * samosa_cost) + (pakoras * pakora_cost) + lassi_cost
    tip = sub_total * 0.25
    total_cost = sub_total + tip
    result = total_cost
    return result

print(solution())