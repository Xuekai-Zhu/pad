def solution():
    # Calculate the cost of 2 scallops
    cost_of_8_scallops = 24.00  # cost of 1 pound of scallops
    cost_of_1_scallop = cost_of_8_scallops/8  # cost of 1 scallop
    cost_of_2_scallops = cost_of_1_scallop*2  # cost of 2 scallops

    # Calculate the total cost of scallops for 8 people
    total_cost = cost_of_2_scallops*8  # Nate is cooking for 8 people
    result = total_cost
    return result

print(solution())