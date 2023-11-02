def solution():
    total_sales = 100  # total sales in dollars
    cost_per_cone = 2  # cost per cone in dollars
    num_cones_sold = total_sales // cost_per_cone  # number of cones sold
    num_free_cones = num_cones_sold // 6  # number of free cones given away
    result = num_free_cones
    return result

print(solution())