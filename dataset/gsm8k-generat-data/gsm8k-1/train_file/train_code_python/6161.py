def solution():
    """A store sells pencils and erasers. It has a rule that for every pencil you buy, you must buy 2 erasers which cost 1/2 
    the price of the pencils. If they sold 20 pencils and earned $80, how much do erasers cost?"""
    pencils_sold = 20
    pencil_price = 80 / 20  # since we know they earned $80 after selling 20 pencils
    eraser_price = pencil_price / 2
    result = eraser_price
    return result

print(solution())