def solution():
    # Calculate the total number of packages to be sent
    total_packages = 1 + 1 + 1 + (3*2) + (2*2*3)  # Two parents, three brothers, three brothers' spouses, and six nieces/nephews

    # Calculate the total cost of sending all the packages
    total_cost = total_packages * 5 

    result = total_cost
    return result

print(solution())