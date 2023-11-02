def solution():
    initial_charge = 0
    charge_time = 45
    percent_charge = 25
    remaining_charge = 100 - percent_charge
    remaining_time = remaining_charge / percent_charge
    total_time = charge_time + remaining_time
    result = total_time
    
    return result

print(solution())