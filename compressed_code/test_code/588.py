def solution():
    
    brad_weight = 54
    jessica_weight = brad_weight / 2
    betty_weight = jessica_weight * 4
    heaviest_pumpkin = max(brad_weight, jessica_weight, betty_weight)
    lightest_pumpkin = min(brad_weight, jessica_weight, betty_weight)
    result = heaviest_pumpkin - lightest_pumpkin
    return result

print(solution())