def solution():
    nike_shoes = 150
    work_boots = 120
    sales_tax = 10
    total_cost = nike_shoes + work_boots
    total_tax = total_cost * (sales_tax / 100)
    final_cost = total_cost + total_tax
    result = final_cost
    return result

print(solution())