def solution():
    """Dan owns an ice cream shop and every sixth customer gets a free ice cream cone. Cones cost $2 each. If he sold $100 worth of cones, how many free ones did he give away?"""
    free_cone_frequency = 6
    cone_cost = 2
    total_sales = 100
    num_cones_sold = total_sales / cone_cost
    num_free_cones_given = num_cones_sold // free_cone_frequency
    result = num_free_cones_given
    return result

print(solution())