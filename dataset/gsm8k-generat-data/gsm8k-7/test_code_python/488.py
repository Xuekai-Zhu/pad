def solution():
    initial_cost = 500
    additional_cost = initial_cost * 2/5
    total_cost = initial_cost + additional_cost
    discount = 0.15
    discounted_price = total_cost * (1 - discount)
    money_needed = discounted_price - initial_cost
    result = money_needed
    return result

print(solution())