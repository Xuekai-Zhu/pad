def solution():
    """A shopping center sells T-shirts at $8 each, a sweater at $18, and a jacket at $80. The jacket is on sale with a 10% discount. The sales tax is 5%. Kevin wants to buy six T-shirts, four sweaters, and five jackets for his children. How much does Kevin have to pay for all the items, including the sales tax?"""
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