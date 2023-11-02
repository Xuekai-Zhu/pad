def solution():
     customers = 100
     tuna_total_weight = 1000
     tuna_desired_weight = 25
     tuna_remaining_weight = tuna_total_weight - (customers * tuna_desired_weight)
     customers_remaining = tuna_remaining_weight / tuna_desired_weight
     result = customers_remaining
     return result

print(solution())