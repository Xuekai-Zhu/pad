def solution():
    """Lola baked 13 mini cupcakes, 10 pop tarts, and 8 blueberry pies. Meanwhile, Lulu made 16 mini cupcakes, 12 pop tarts, and 14 blueberry pies. How many pastries have Lola and Lulu made altogether?"""
    lola_mini_cupcakes = 13
    lola_pop_tarts = 10
    lola_blueberry_pies = 8

    lulu_mini_cupcakes = 16
    lulu_pop_tarts = 12
    lulu_blueberry_pies = 14

    total_pastries = (lola_mini_cupcakes + lulu_mini_cupcakes) + (lola_pop_tarts + lulu_pop_tarts) + (lola_blueberry_pies + lulu_blueberry_pies)

    result = total_pastries
    return result

print(solution())