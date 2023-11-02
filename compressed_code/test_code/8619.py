def solution():
    
    cost_per_machine = 3600 + 4500
    price_per_machine = 180
    machines_to_break_even = cost_per_machine / (price_per_machine * 1.0)
    result = machines_to_break_even
    return result

print(solution())