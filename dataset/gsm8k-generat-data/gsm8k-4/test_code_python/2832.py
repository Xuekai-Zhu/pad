def solution():
    """During April, the baker sold 453 cakes at $12 and 126 pies at $7. How much did the baker earn?"""
    # Define the number of cakes sold, the price per cake, the number of pies sold, and the price per pie
    cakes_sold = 453
    cake_price = 12
    pies_sold = 126
    pie_price = 7

    # Calculate the earnings from selling cakes
    cake_earnings = cakes_sold * cake_price

    # Calculate the earnings from selling pies
    pie_earnings = pies_sold * pie_price

    # Calculate the total earnings
    total_earnings = cake_earnings + pie_earnings

    # return the result
    result = total_earnings
    return result

print(solution())