def solution():
    """At A.T. Cross Luxury Pens, a pencil sells at twenty-five cents while a pen sells at fifteen cents. Bowen buys 40 pens
    and 2/5 times more pencils than pens from A.T. Cross Luxury Pens. Calculate the total amount of money Bowen spends."""
    # Define the prices
    pen_price = 15
    pencil_price = 25

    # Calculate the number of pencils Bowen buys
    pencil_ratio = 2/5
    pencil_multiplier = 1 + pencil_ratio
    pen_count = 40
    pencil_count = int(pencil_multiplier * pen_count)

    # Calculate the total spent
    total_spent = (pen_count * pen_price) + (pencil_count * pencil_price)

    result = total_spent
    return result

print(solution())