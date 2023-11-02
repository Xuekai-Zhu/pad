def solution():
    single_price = 2.25
    dozen_price = 24/12
    savings = (single_price - dozen_price) * 100  # in cents
    result = savings
    return result

print(solution())