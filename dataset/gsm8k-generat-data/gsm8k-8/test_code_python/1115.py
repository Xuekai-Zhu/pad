def solution():
    # Calculate the cost per jumbo scallop
    cost_per_pound = 24.00
    scallops_per_pound = 8
    cost_per_scallop = cost_per_pound / scallops_per_pound

    # Determine the total number of scallops needed
    scallops_per_person = 2
    total_scallops_needed = scallops_per_person * 8

    # Calculate the total cost of the scallops
    total_cost = total_scallops_needed * cost_per_scallop
    result = total_cost
    return result

print(solution())