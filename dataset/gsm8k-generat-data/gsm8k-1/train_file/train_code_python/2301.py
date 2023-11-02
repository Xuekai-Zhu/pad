def solution():
    """Each year a store decreased the price of a certain model of TV by $35. If the price in 2001 was $1950, what was the price in 2009?"""
    price_in_2001 = 1950
    years_passed = 8 #2009-2001=8
    price_decrease_per_year = 35
    total_price_decrease = years_passed * price_decrease_per_year
    price_in_2009 = price_in_2001 - total_price_decrease
    result = price_in_2009
    return result

print(solution())