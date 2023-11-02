def solution():
    plates = 100
    rice_cost = 0.1
    chicken_cost = 0.4
    rice_total = plates * rice_cost
    chicken_total = plates * chicken_cost
    total_cost = rice_total + chicken_total
    result = total_cost
    return result

print(solution())