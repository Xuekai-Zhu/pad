def solution():
    """John buys 500 newspapers. Each newspaper sells for $2. He sells 80% of them. He buys them all for 75% less than the price at which he sells them. How much profit does he make?"""
    num_newspapers = 500
    sale_price = 2
    percent_sold = 80
    num_sold = num_newspapers * (percent_sold / 100)
    purchase_price = sale_price * (1 - 0.75)
    cost = num_newspapers * purchase_price
    revenue = num_sold * sale_price
    profit = revenue - cost
    result = profit
    return result

print(solution())