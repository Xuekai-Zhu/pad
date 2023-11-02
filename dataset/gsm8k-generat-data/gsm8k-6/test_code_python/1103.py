def solution():
    # Calculate the cost of flowers per centerpiece
    cost_per_centerpiece = 8*15 + 2*(8*15) + x*15  # x is the number of lilies in each centerpiece
    # Set the total cost equal to $2700
    total_cost = 6*cost_per_centerpiece
    # Solve for x
    x = (2700 - 6*8*15 - 6*(2*(8*15))) / (6*15)
    result = x
    return result

print(solution())