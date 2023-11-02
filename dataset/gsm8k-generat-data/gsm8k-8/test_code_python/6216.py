def solution():
    # Define the original budget and the new budget with the added 20%
    original_budget = 1000
    new_budget = 1.2 * original_budget

    # Calculate how many softballs they can buy with the new budget
    num_softballs = new_budget // 9

    result = num_softballs
    return result

print(solution())