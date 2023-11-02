def solution():
    
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