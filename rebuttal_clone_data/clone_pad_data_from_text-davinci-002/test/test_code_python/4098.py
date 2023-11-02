def solution():
    money_initial = 40
    quarters_initial = 200
    money_given = 5
    quarters_given = 120
    money_leftover = money_initial - money_given
    quarters_leftover = quarters_initial - quarters_given
    total_leftover = money_leftover + (quarters_leftover * 0.25)
    result = total_leftover
    return result

print(solution())