def solution():
    cost_per_cone = 2
    total_sales = 100
    num_free_cones = total_sales // (cost_per_cone * 6)
    result = num_free_cones
    return result

print(solution())