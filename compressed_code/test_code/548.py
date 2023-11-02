def solution():
    
    samosas_cost = 3 * 2
    pakoras_cost = 4 * 3
    lassi_cost = 2
    subtotal = samosas_cost + pakoras_cost + lassi_cost
    tip = 0.25 * subtotal
    total_cost = subtotal + tip
    result = total_cost
    return result

print(solution())