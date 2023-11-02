def solution():
    initial_lumber_cost = 450
    initial_nails_cost = 30
    initial_fabric_cost = 80

    lumber_inflation = 0.2
    nails_inflation = 0.1
    fabric_inflation = 0.05

    # Calculate the new costs after inflation
    new_lumber_cost = initial_lumber_cost * (1 + lumber_inflation)
    new_nails_cost = initial_nails_cost * (1 + nails_inflation)
    new_fabric_cost = initial_fabric_cost * (1 + fabric_inflation)

    # Calculate the difference between the new cost and the initial cost
    total_increase = new_lumber_cost + new_nails_cost + new_fabric_cost - \
                     initial_lumber_cost - initial_nails_cost - initial_fabric_cost
    result = total_increase
    return result

print(solution())