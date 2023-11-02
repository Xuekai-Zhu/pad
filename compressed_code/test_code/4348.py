def solution():
    
    total_tuna_weight = 10 * 200
    tuna_per_customer = 25
    max_customers_served = total_tuna_weight // tuna_per_customer
    customers_without_fish = 100 - max_customers_served
    result = customers_without_fish
    return result

print(solution())