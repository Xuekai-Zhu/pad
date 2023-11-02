def solution():
    
    machines = 10
    bearings_per_machine = 30
    normal_price = 1
    sale_price = 0.75
    discount = 0.2
    normal_total_cost = machines * bearings_per_machine * normal_price
    sale_total_cost = machines * bearings_per_machine * sale_price * (1 - discount)
    saved_money = normal_total_cost - sale_total_cost
    result = saved_money
    return result

print(solution())