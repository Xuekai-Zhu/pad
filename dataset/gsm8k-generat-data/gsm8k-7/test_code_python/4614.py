def solution():
    check_amount = 50

    # Let x be the original balance before the check deposit
    # The new balance after the check deposit will be x + 50
    # According to the problem, the check is worth a quarter of the new balance
    # 50 = 0.25 * (x + 50)
    x = (50 / 0.25) - 50

    result = x
    return result

print(solution())