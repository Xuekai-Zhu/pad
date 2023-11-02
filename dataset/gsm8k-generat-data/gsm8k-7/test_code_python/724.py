def solution():
    money_left = 24
    fraction_spent = 3/7

    # Calculate the amount of money Jenny had before spending
    original_money = money_left / (1 - fraction_spent)

    # Calculate half of Jenny's original amount of money
    half_money = original_money / 2
    result = half_money
    return result

print(solution())