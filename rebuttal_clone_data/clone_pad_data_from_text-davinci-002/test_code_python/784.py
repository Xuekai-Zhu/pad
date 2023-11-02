def solution():
    brad_pumpkin = 54
    jessica_pumpkin = brad_pumpkin / 2
    betty_pumpkin = jessica_pumpkin * 4
    heaviest_pumpkin = max(brad_pumpkin, jessica_pumpkin, betty_pumpkin)
    lightest_pumpkin = min(brad_pumpkin, jessica_pumpkin, betty_pumpkin)
    result = heaviest_pumpkin - lightest_pumpkin
    return result

print(solution())