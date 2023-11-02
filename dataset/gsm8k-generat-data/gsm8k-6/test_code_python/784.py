def solution():
    # Find the weights of the pumpkins
    brad_weight = 54
    jessica_weight = brad_weight / 2  # Jessica's pumpkin is half the weight of Brad's
    betty_weight = jessica_weight * 4  # Betty's pumpkin is 4 times the weight of Jessica's

    # Find the heaviest and lightest pumpkins
    heaviest_pumpkin = max(brad_weight, jessica_weight, betty_weight)
    lightest_pumpkin = min(brad_weight, jessica_weight, betty_weight)

    # Find the difference between the heaviest and lightest pumpkins
    difference = heaviest_pumpkin - lightest_pumpkin
    result = difference
    return result

print(solution())