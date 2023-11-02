def solution():
    
    tshirt_price = 8
    sweater_price = 18
    jacket_price = 80
    jacket_discount = 0.1
    tshirt_quantity = 6
    sweater_quantity = 4
    jacket_quantity = 5

    tshirt_total = tshirt_price * tshirt_quantity
    sweater_total = sweater_price * sweater_quantity
    jacket_total = (jacket_price * (1-jacket_discount)) * jacket_quantity

    sub_total = tshirt_total + sweater_total + jacket_total
    sales_tax = 0.05 * sub_total
    total_cost = sub_total + sales_tax

    result = total_cost
    return result

print(solution())