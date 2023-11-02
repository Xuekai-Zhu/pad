def solution():
    # Define variables for Antoinette's weight and Rupert's weight
    ant_weight = 0
    rup_weight = 0
    
    # Use algebra to solve for the variables
    # A = 2R - 7
    # A + R = 98
    # Substitute the first equation into the second to get:
    # 2R - 7 + R = 98
    # Simplify to get:
    # 3R = 105
    # Solve for R:
    rup_weight = 35
    ant_weight = 2*rup_weight - 7

    result = ant_weight
    return result

print(solution())