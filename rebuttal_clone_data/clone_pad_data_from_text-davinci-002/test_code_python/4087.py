def solution():
    saved_money = 20000
    cost_per_foot = 1500
    license_and_registration = 500
    docking_fees = 3 * license_and_registration
    total_cost = cost_per_foot + license_and_registration + docking_fees
    length_of_boat = saved_money / total_cost
    result = length_of_boat
    
    return result

print(solution())