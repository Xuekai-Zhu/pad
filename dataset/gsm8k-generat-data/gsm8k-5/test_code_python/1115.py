def solution():
    # Calculate the cost per scallop
    cost_per_pound = 24.00
    scallops_per_pound = 8
    cost_per_scallop = cost_per_pound / scallops_per_pound

    # Calculate the total number of scallops needed
    scallops_per_person = 2
    total_scallops = scallops_per_person * 8

    # Calculate the total cost of the scallops
    total_cost = cost_per_scallop * total_scallops
    result = total_cost
    return result

print(solution())