def solution():
    width = 7
    height = 8
    cost_per_sqft = 40

    # Calculate the total area of the quilt in square feet
    total_area = width * height
    
    # Calculate the total cost of the quilt
    total_cost = total_area * cost_per_sqft
    result = total_cost
    return result

print(solution())