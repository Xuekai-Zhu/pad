def solution():
    num_scallops_per_pound = 8
    cost_per_pound = 24.0
    num_scallops_per_person = 2
    num_people = 8

    # Calculate the total number of scallops needed
    total_scallops = num_scallops_per_person * num_people

    # Calculate the total number of pounds of scallops needed
    total_pounds_scallops = total_scallops / num_scallops_per_pound

    # Calculate the total cost of all scallops
    total_cost = total_pounds_scallops * cost_per_pound
    result = total_cost
    return result

print(solution())