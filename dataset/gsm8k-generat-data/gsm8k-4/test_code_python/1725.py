def solution():
    """Mike has to get an x-ray and an MRI.  The x-ray is $250 and the MRI is triple that cost.  Insurance covers 80%.  How much did he pay?"""
    # Define the cost of the x-ray and the MRI
    x_ray_cost = 250
    mri_cost = x_ray_cost * 3

    # Calculate the total cost before insurance coverage
    total_cost = x_ray_cost + mri_cost

    # Calculate the amount covered by insurance
    insurance_coverage = total_cost * 0.8

    # Calculate the amount Mike has to pay out of pocket
    out_of_pocket = total_cost - insurance_coverage
    
    # return the result
    result = out_of_pocket
    return result

print(solution())