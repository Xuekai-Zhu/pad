def solution():
    """Dan owns an ice cream shop and every sixth customer gets a free ice cream cone. Cones cost $2 each. If he sold $100 worth of cones, how many free ones did he give away?"""
    # Define the cost of one ice cream cone
    cone_cost = 2

    # Calculate the total number of ice cream cones sold
    total_cones_sold = 100 / cone_cost

    # Calculate the number of free cones given away
    free_cones = (total_cones_sold // 6)

    result = free_cones
    return result

print(solution())