def solution():
    """Kylie has 5 daisies. Her sister gave her another 9 daisies. Kylie then gave half her daisies to her mother. How many daisies does Kylie have left?"""
    kylie_daisies = 5
    sister_daisies = 9
    total_daisies = kylie_daisies + sister_daisies
    kylie_daisies = total_daisies // 2
    result = kylie_daisies
    return result

print(solution())