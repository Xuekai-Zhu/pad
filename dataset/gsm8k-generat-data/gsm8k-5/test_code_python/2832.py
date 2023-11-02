def solution():
    # Calculate the total earnings from selling cakes
    cakes_sold = 453
    cake_price = 12
    total_cake_earnings = cakes_sold * cake_price

    # Calculate the total earnings from selling pies
    pies_sold = 126
    pie_price = 7
    total_pie_earnings = pies_sold * pie_price

    # Calculate the total earnings from selling both cakes and pies
    total_earnings = total_cake_earnings + total_pie_earnings
    result = total_earnings
    return result

print(solution())