def solution():
    # Define the weights of the pumpkins
    brad_weight = 54
    jessica_weight = brad_weight / 2
    betty_weight = jessica_weight * 4

    # Find the heaviest and lightest pumpkins
    heaviest_pumpkin = max(brad_weight, jessica_weight, betty_weight)
    lightest_pumpkin = min(brad_weight, jessica_weight, betty_weight)

    # Calculate the difference between the heaviest and lightest pumpkins
    difference = heaviest_pumpkin - lightest_pumpkin
    result = difference
    return result

print(solution())