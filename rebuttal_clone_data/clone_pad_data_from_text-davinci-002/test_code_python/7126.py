def solution():
    washing_machine_cost = 100
    dryer_cost = washing_machine_cost - 30
    total_cost = washing_machine_cost + dryer_cost
    discount = total_cost * .1
    total_cost_after_discount = total_cost - discount
    result = total_cost_after_discount
    return result

print(solution())