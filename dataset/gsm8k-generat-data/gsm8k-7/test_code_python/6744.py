def solution():
    cherry_price = 8
    total_price = 1600
    missing_price = 400
    amount_paid = total_price - missing_price
    cherry_weight = amount_paid / cherry_price
    result = cherry_weight
    return result

print(solution())