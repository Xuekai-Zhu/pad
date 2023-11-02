def solution():
    cost_of_lunch = 100
    sales_tax_rate = 4
    tip_rate = 6
    sales_tax = cost_of_lunch * (sales_tax_rate / 100)
    tip = cost_of_lunch * (tip_rate / 100)
    total_cost = cost_of_lunch + sales_tax + tip
    result = total_cost
    return result

print(solution())