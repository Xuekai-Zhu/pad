def solution():
    """At A.T. Cross Luxury Pens, a pencil sells at twenty-five cents while a pen sells at fifteen cents. Bowen buys 40 pens and 2/5 times more pencils than pens from A.T. Cross Luxury Pens. Calculate the total amount of money Bowen spends."""
    pen_price = 0.15
    pencil_price = 0.25
    num_pens = 40
    num_pencils = int(num_pens * (2/5 + 1))
    total_spent = num_pens * pen_price + num_pencils * pencil_price
    result = total_spent
    return result

print(solution())