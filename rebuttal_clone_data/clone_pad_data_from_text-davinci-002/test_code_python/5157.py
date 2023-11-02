def solution():
    cost = 15.00
    tax_rate = 20
    tax_amount = cost * (tax_rate / 100)
    total_cost = cost + tax_amount
    given = 20
    change = given - total_cost
    tip = change
    result = tip
    return result

print(solution())