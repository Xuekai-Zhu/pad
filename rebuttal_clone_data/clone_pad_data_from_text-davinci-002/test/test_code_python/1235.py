def solution():
    cost = 200
    tax_rate = 15
    tax_amount = cost * (tax_rate / 100)
    total_cost = cost + tax_amount
    result = total_cost
    return result

print(solution())