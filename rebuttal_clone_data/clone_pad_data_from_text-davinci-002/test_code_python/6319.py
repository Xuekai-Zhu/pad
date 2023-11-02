def solution():
    number_of_pants = 10
    percent_off = 20
    pants_cost = 45
    cost_after_discount = (1 - (percent_off / 100)) * pants_cost
    tax = 0.1
    cost_after_tax = (1 + tax) * cost_after_discount
    total_cost = cost_after_tax * number_of_pants
    result = total_cost
    return result

print(solution())