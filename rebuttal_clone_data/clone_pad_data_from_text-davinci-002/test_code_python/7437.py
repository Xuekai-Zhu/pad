def solution():
    price_per_circle = 1
    money_earned = 5
    pieces_sold = 100 + (2 * 45) + (3 * 50)
    money_made = pieces_sold * price_per_circle
    quadruple_pieces_sold = money_earned - money_made
    result = quadruple_pieces_sold
    return result

print(solution())