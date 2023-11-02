def solution():
    nikes_price = 150
    work_boots_price = 120
    tax_rate = 0.1  # 10% tax

    # Calculate the total cost of the shoes without tax
    total_shoes_cost = nikes_price + work_boots_price

    # Calculate the cost of the tax
    tax_cost = total_shoes_cost * tax_rate

    # Calculate the total cost of the shoes with tax
    total_cost = total_shoes_cost + tax_cost
    result = total_cost
    return result

print(solution())