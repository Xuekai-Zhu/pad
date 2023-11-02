def solution():
    base_salary = 3000
    commission = 0.02
    total_earnings = 8000
    house_a = total_earnings / (1 + 3 * commission + 2 * commission - 110_000 / commission)
    result = house_a
    return result

print(solution())