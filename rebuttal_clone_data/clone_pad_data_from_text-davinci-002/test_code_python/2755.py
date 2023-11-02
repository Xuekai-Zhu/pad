def solution():
    pencil_price = 0.25
    pen_price = 0.15
    pens_bought = 40
    pencils_bought = pens_bought * 2/5
    total_cost = pencils_bought * pencil_price + pens_bought * pen_price
    result = total_cost
    return result

print(solution())