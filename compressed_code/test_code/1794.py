def solution():
    
    start_year_price = 1950
    end_year = 2009
    num_years = end_year - 2001
    price_decrease_per_year = 35
    end_year_price = start_year_price - (num_years * price_decrease_per_year)
    result = end_year_price
    return result

print(solution())