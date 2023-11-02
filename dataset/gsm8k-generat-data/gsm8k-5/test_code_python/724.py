def solution():
    money_left = 24  # Jenny had $24 left
    fraction_spent = 3/7  # Jenny spent 3/7 of her money
    fraction_left = 1 - fraction_spent  # Fraction of money Jenny has left
    original_money = money_left / fraction_left  # Calculate Jenny's original amount of money

    # Calculate half of Jenny's original amount of money
    half_money = original_money / 2
    result = half_money
    return result

print(solution())