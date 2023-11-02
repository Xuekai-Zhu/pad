def solution():
    """Zayne sells bracelets for $5 each and two for $8. If he started with 30 bracelets and made $60 from selling bracelets for $5 each, how much in total did he make from selling his bracelets?"""
    starting_bracelets = 30
    price_single = 5
    price_double = 8
    sold_single = 60 // price_single
    sold_double = (starting_bracelets - sold_single) // 2
    total_sold = sold_single + sold_double
    total_profit = (sold_single * price_single) + (sold_double * price_double)
    result = total_profit
    return result

print(solution())