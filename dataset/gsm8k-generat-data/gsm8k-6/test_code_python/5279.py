def solution():
    # Calculate this year's production and the number of phones sold
    this_year_production = 2 * 5000  # twice as many phones as last year
    sold_phones = this_year_production / 4  # a quarter of this year's production is sold

    # Calculate the number of phones left in the factory
    phones_left = this_year_production - sold_phones
    result = phones_left
    return result

print(solution())