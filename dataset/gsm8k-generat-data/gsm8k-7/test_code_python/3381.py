def solution():
    num_shirts = 5
    cost_of_3_shirts = 15
    cost_of_2_shirts = 20

    # Calculate the total cost of the 3 cheaper shirts
    total_cost_of_3_shirts = cost_of_3_shirts * 3

    # Calculate the total cost of the 2 more expensive shirts
    total_cost_of_2_shirts = cost_of_2_shirts * 2

    # Calculate the total cost of all 5 shirts
    total_cost = total_cost_of_3_shirts + total_cost_of_2_shirts
    result = total_cost
    return result

print(solution())