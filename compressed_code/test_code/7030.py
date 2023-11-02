def solution():
    
    charge_time = 10
    use_time_per_charge = 2
    partial_charge_time = 3/5 * charge_time
    total_use_time = use_time_per_charge * partial_charge_time
    result = total_use_time
    return result

print(solution())