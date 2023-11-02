def solution():
    """Marcus ordered 5 croissants at $3.00 apiece, 4 cinnamon rolls at $2.50 each, 3 mini quiches for $4.00 apiece and 13 blueberry muffins that were $1.00 apiece. At check out, Marcus shows his loyalty card that gives him 10% off of his purchase. What is Marcus' total bill?"""
    croissant_cost = 3.00
    croissant_qty = 5
    cinnamon_roll_cost = 2.50
    cinnamon_roll_qty = 4
    mini_quiche_cost = 4.00
    mini_quiche_qty = 3
    muffin_cost = 1.00
    muffin_qty = 13

    subtotal = (croissant_cost * croissant_qty) + (cinnamon_roll_cost *
                                                   cinnamon_roll_qty) + (mini_quiche_cost*mini_quiche_qty) + (muffin_cost*muffin_qty)
    discount = .1*subtotal
    total_cost = subtotal-discount

    result = total_cost
    return result

print(solution())