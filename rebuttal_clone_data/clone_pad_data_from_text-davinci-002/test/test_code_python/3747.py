def solution():
    computers_repaired = 20
    computers_unfixable = computers_repaired * 0.20
    computers_needed_parts = computers_repaired * 0.40
    computers_fixed_right_away = computers_repaired - computers_unfixable - computers_needed_parts
    result = computers_fixed_right_away
    
    return result

print(solution())