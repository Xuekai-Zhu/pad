def solution():
    """During April, the baker sold 453 cakes at $12 and 126 pies at $7. How much did the baker earn?"""
    cake_price = 12
    pie_price = 7
    num_cakes_sold = 453
    num_pies_sold = 126
    total_earned = (cake_price * num_cakes_sold) + (pie_price * num_pies_sold)
    result = total_earned
    return result

print(solution())