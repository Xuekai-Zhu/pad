def solution():
    """In a stationery store, there are three kinds of pencils. A pencil with an eraser, which costs $0.8 each, a regular pencil for $0.5 each, and a short pencil for $0.4 each. This store was able to sell 200 pencils with an eraser, 40 regular pencils, and 35 short pencils. How much money did the store make from these sales?"""
    eraser_pencil_price = 0.8
    regular_pencil_price = 0.5
    short_pencil_price = 0.4
    eraser_pencils_sold = 200
    regular_pencils_sold = 40
    short_pencils_sold = 35
    total_money_made = eraser_pencil_price * eraser_pencils_sold + regular_pencil_price * regular_pencils_sold + short_pencil_price * short_pencils_sold
    result = total_money_made
    return result

print(solution())