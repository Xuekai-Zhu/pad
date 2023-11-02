def solution():
    washing_machine_cost = 100
    dryer_cost = washing_machine_cost - 30
    total_cost = washing_machine_cost + dryer_cost
    discount = 0.1 # 10% discount
    discounted_cost = total_cost * (1 - discount)
    result = discounted_cost
    return result

print(solution())