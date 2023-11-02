def solution():
    
    long_sleeved_cost = 15
    num_long_sleeved = 4
    total_long_sleeved_cost = long_sleeved_cost * num_long_sleeved
    total_cost = 80
    striped_cost = 10
    num_striped = (total_cost - total_long_sleeved_cost) / striped_cost
    result = num_striped
    return result

print(solution())