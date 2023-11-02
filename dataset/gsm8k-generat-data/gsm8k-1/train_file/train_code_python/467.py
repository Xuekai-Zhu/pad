def solution():
    """A shopping center sells T-shirts at $8 each, a sweater at $18, and a jacket at $80. The jacket is on sale with a 10% discount. The sales tax is 5%. Kevin wants to buy six T-shirts, four sweaters, and five jackets for his children. How much does Kevin have to pay for all the items, including the sales tax?"""
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