def solution():
    # Calculate the cost of each item
    cost_kiddie_scoop = 3
    cost_regular_scoop = 4
    cost_double_scoop = 6

    # Calculate the total cost for each family member
    cost_mr_martin = cost_regular_scoop
    cost_mrs_martin = cost_regular_scoop
    cost_child_1 = cost_kiddie_scoop
    cost_child_2 = cost_kiddie_scoop
    cost_teen_1 = cost_double_scoop
    cost_teen_2 = cost_double_scoop
    cost_teen_3 = cost_double_scoop

    # Calculate the total cost for the Martin family
    total_cost = (cost_mr_martin + cost_mrs_martin + cost_child_1 + cost_child_2 + cost_teen_1 + cost_teen_2 + cost_teen_3)

    result = total_cost
    return result

print(solution())