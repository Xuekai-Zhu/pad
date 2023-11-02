def solution():
    money_left = 24  # Anna has $24 left
    money_spent = 1/4  # Anna spent 1/4 of her money

    # Calculate the original amount of money Anna had
    original_money = money_left / (1 - money_spent)
    result = original_money
    return result

print(solution())