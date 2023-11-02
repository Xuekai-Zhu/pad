def solution():
    money_left = 24
    fraction_spent = 1/4

    # Calculate the fraction of money Anna has left
    fraction_left = 1 - fraction_spent

    # Calculate the original amount of money Anna had
    original_money = money_left / fraction_left
    result = original_money
    return result

print(solution())