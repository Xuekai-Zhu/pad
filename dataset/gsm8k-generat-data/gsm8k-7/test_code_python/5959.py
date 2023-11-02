def solution():
    lola_cupcakes = 13
    lola_pop_tarts = 10
    lola_pies = 8

    lulu_cupcakes = 16
    lulu_pop_tarts = 12
    lulu_pies = 14

    # Calculate the total number of each pastry made
    total_cupcakes = lola_cupcakes + lulu_cupcakes
    total_pop_tarts = lola_pop_tarts + lulu_pop_tarts
    total_pies = lola_pies + lulu_pies

    # Calculate the total number of pastries made altogether
    total_pastries = total_cupcakes + total_pop_tarts + total_pies
    result = total_pastries
    return result

print(solution())