def solution():
    # Calculate the total number of cones sold
    total_cones_sold = 100 / 2
    
    # Calculate the number of customers who received a free cone
    free_cone_customers = total_cones_sold // 6

    result = free_cone_customers
    return result

print(solution())