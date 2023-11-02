def solution():
    # Calculate the number of each software package needed
    num_40_package = 10
    num_60_package = 5

    # Calculate the cost of each package
    cost_40_package = num_40_package * 40
    cost_60_package = num_60_package * 60

    # Calculate the total cost of each package
    total_cost_40 = cost_40_package * 2
    total_cost_60 = cost_60_package

    # Calculate the savings by buying the $60 package
    savings = total_cost_40 - total_cost_60
    result = savings
    return result

print(solution())