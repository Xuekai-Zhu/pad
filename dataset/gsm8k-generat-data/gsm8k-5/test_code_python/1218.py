def solution():
    nike_price = 150  # Price of Nike shoes
    work_boots_price = 120  # Price of work boots
    total_price = nike_price + work_boots_price  # Total price before tax
    tax_rate = 0.1  # Tax rate of 10%
    tax_amount = total_price * tax_rate  # Tax on the total price
    total_cost = total_price + tax_amount  # Total cost including tax
    result = total_cost
    return result

print(solution())