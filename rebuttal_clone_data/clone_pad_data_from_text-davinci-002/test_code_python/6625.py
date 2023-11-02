def solution():
    apples_bought = 48
    apples_needed_for_full_size_pies = 24
    apples_needed_for_mini_pies = apples_bought / 2
    apples_leftover = apples_bought - (apples_needed_for_full_size_pies + apples_needed_for_mini_pies)
    result = apples_leftover
    return result

print(solution())