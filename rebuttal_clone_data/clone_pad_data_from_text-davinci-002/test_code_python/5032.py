def solution():
    tablet_charge_time = 53
    phone_charge_time = 26
    phone_charge = 0.5
    tablet_charge = 1
    
    total_charge_time = tablet_charge_time + (phone_charge_time * phone_charge)
    
    result = total_charge_time
    
    return result

print(solution())