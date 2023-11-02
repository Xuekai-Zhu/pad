def solution():
    """Lola baked 13 mini cupcakes, 10 pop tarts, and 8 blueberry pies. Meanwhile, Lulu made 16 mini cupcakes, 12 pop tarts, and 14 blueberry pies. How many pastries have Lola and Lulu made altogether?"""
    
    # Define the number of pastries made by Lola
    lola_cupcakes = 13
    lola_pop_tarts = 10
    lola_pies = 8

    # Define the number of pastries made by Lulu
    lulu_cupcakes = 16
    lulu_pop_tarts = 12
    lulu_pies = 14

    # Calculate the total number of pastries made
    total_cupcakes = lola_cupcakes + lulu_cupcakes
    total_pop_tarts = lola_pop_tarts + lulu_pop_tarts
    total_pies = lola_pies + lulu_pies
    total_pastries = total_cupcakes + total_pop_tarts + total_pies

    # Display the total number of pastries
    result = total_pastries
    return result

print(solution())