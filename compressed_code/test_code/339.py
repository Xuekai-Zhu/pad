def solution():
    
    tshirt_price = 8
    sweater_price = 18
    jacket_price = 80
    jacket_discount = 0.1
    sales_tax = 0.05
    tshirt_total = 6 * tshirt_price
    sweater_total = 4 * sweater_price
    jacket_total = (1 - jacket_discount) * (5 * jacket_price)
    subtotal = tshirt_total + sweater_total + jacket_total
    tax_amount = sales_tax * subtotal
    total_price = subtotal + tax_amount
    result = total_price
    return result

print(solution())