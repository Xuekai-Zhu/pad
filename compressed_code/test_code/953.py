def solution():
    
    initial_charge = 0
    current_charge = 0.25
    time_until_current_charge = 45
    remaining_charge_needed = 1 - current_charge
    time_needed_to_complete_charge = (remaining_charge_needed / 0.25) * time_until_current_charge
    result = time_needed_to_complete_charge
    return result

print(solution())