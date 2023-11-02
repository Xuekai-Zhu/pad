def solution():
    """A shop sells school supplies. One notebook is sold at $1.50 each, a pen at $0.25 each, a calculator at $12 each, and a geometry set at $10. Daniel is an engineering student, and he wants to buy five notebooks, two pens, one calculator, and one geometry set. The shop gives a 10% discount on all the purchased items. How much does Daniel have to spend on all the items he wants to buy?"""
    notebook_price = 1.5
    pen_price = 0.25
    calculator_price = 12
    geometry_set_price = 10
    notebook_quantity = 5
    pen_quantity = 2
    calculator_quantity = 1
    geometry_set_quantity = 1
    total_price = (notebook_price * notebook_quantity) + (pen_price * pen_quantity) + (
                calculator_price * calculator_quantity) + (geometry_set_price * geometry_set_quantity)
    discount = total_price * 0.10
    discounted_price = total_price - discount
    result = discounted_price
    return result

print(solution())