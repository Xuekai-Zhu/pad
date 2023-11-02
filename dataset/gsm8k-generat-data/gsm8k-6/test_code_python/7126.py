def solution():
    washing_machine_cost = 100
    dryer_cost = washing_machine_cost - 30
    total_cost = washing_machine_cost + dryer_cost
    discount = 0.1 * total_cost
    discounted_total = total_cost - discount
    result = discounted_total
    return result

print(solution())