def solution():
    initial_charge = 0
    current_charge = 25
    time_to_reach_current_charge = 45
    time_to_reach_full_charge = (100-current_charge) * (time_to_reach_current_charge/25)
    result = time_to_reach_full_charge
    return result

print(solution())