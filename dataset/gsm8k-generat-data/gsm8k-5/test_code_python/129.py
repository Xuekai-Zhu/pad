def solution():
    cost_per_cone = 2  # An ice cream cone costs $2
    total_sales = 100  # Dan sold $100 worth of cones

    # Calculate the number of regular cones sold
    regular_cones_sold = total_sales // cost_per_cone

    # Calculate the number of free cones given away (every sixth customer)
    free_cones_given = regular_cones_sold // 6

    result = free_cones_given
    return result

print(solution())