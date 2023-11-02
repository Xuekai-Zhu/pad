def solution():
    # Define the cost of trimming up each boxwood and shaping it into a fancy shape
    trim_up_cost = 5.00
    fancy_shape_cost = 15.00

    # Calculate the cost of trimming up all 30 boxwoods
    trim_up_total_cost = trim_up_cost * 30

    # Calculate the cost of shaping the 4 specified boxwoods into spheres
    sphere_cost = fancy_shape_cost * 4

    # Calculate the total cost for Neil's services
    total_cost = trim_up_total_cost + sphere_cost
    result = total_cost
    return result

print(solution())