def solution():
    """Dan owns an ice cream shop and every sixth customer gets a free ice cream cone. Cones cost $2 each. If he sold $100 worth of cones, how many free ones did he give away?"""
    # Define the cost of each cone and the total revenue
    cone_cost = 2
    total_revenue = 100

    # Calculate the number of cones sold
    cones_sold = total_revenue / cone_cost

    # Calculate the number of free cones given away
    free_cones = cones_sold // 6

    # return the result
    result = free_cones
    return result

print(solution())