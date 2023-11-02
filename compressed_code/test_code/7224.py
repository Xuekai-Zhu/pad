def solution():
    
    total_100mg_sales = 80
    total_500mg_sales = 60
    cost_per_100mg_capsule = 5
    cost_per_500mg_capsule = 2
    total_100mg_capsules = total_100mg_sales / cost_per_100mg_capsule
    total_500mg_capsules = total_500mg_sales / cost_per_500mg_capsule
    total_capsules = (total_100mg_capsules + total_500mg_capsules) * 2
    result = total_capsules
    return result

print(solution())