def solution():
    """Elizabeth has 20 dollars and wants to buy pens and pencils. Each pencil costs $1.60 and each pen cost 2 dollars. How many pencils can she buy with her 20 dollars if she wants 6 pens?"""
    num_pens = 6
    pen_price = 2
    pencil_price = 1.6
    total_spent = num_pens * pen_price + (20 - num_pens * pen_price)
    num_pencils = int(total_spent / pencil_price)
    result = num_pencils
    return result

print(solution())