def solution():
    """During April, the baker sold 453 cakes at $12 and 126 pies at $7. How much did the baker earn?"""
    cakes_sold = 453
    cake_price = 12
    pies_sold = 126
    pie_price = 7
    total_cake_earnings = cakes_sold * cake_price
    total_pie_earnings = pies_sold * pie_price
    total_earnings = total_cake_earnings + total_pie_earnings
    result = total_earnings
    return result

print(solution())