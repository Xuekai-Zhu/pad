def solution():
    """Dan owns an ice cream shop and every sixth customer gets a free ice cream cone. Cones cost $2 each. If he sold $100 worth of cones, how many free ones did he give away?"""
    cones_sold = 100 // 2    # find number of cones sold by dividing total revenue by price per cone
    free_cone_frequency = 6   # every 6th customer gets a free ice cream cone
    free_cone_count = cones_sold // free_cone_frequency
    result = free_cone_count
    return result

print(solution())