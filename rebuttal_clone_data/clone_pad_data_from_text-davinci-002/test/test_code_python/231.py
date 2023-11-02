def solution():
    number_of_carwashes = 20
    discount = 60
    cost_per_carwash = 15
    total_cost = number_of_carwashes * cost_per_carwash
    cost_after_discount = total_cost * (discount / 100)
    result = cost_after_discount
    return result

print(solution())