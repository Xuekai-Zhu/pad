def solution():
    cost_per_shirt = 15
    percent_off = 20
    number_of_shirts = 5
    number_of_fandoms = 4
    percent_tax = 10
    cost_before_tax = cost_per_shirt * number_of_shirts * number_of_fandoms
    cost_after_discount = cost_before_tax - (cost_before_tax * (percent_off/100))
    total_cost = cost_after_discount + (cost_after_discount * (percent_tax/100))
    result = total_cost

    return result

print(solution())