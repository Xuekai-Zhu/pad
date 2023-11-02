def solution():
    brad_weight = 54
    jessica_weight = brad_weight / 2
    betty_weight = jessica_weight * 4

    # Find the heaviest and lightest pumpkin weights
    heaviest_weight = max(brad_weight, jessica_weight, betty_weight)
    lightest_weight = min(brad_weight, jessica_weight, betty_weight)

    # Calculate the difference between the heaviest and lightest pumpkins
    difference = heaviest_weight - lightest_weight
    result = difference
    return result

print(solution())