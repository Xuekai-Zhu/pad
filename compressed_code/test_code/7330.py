def solution():
    
    paintbrush_cost = 1.5
    paints_cost = 4.35
    easel_cost = 12.65
    total_cost = paintbrush_cost + paints_cost + easel_cost
    money_available = 6.5
    money_needed = total_cost - money_available
    result = money_needed
    return result

print(solution())