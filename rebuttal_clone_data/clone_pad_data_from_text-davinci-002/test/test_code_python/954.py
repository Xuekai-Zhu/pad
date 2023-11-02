def solution():
    shampoo_cost = 10
    conditioner_cost = 10
    lotion_cost = 6
    total_cost = shampoo_cost + conditioner_cost + (lotion_cost * 3)
    free_shipping_threshold = 50
    money_needed = free_shipping_threshold - total_cost
    result = money_needed
    return result

print(solution())