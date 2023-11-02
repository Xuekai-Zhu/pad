def solution():
    last_year_production = 5000
    this_year_production = last_year_production * 2
    sold_fraction = 1/4

    # Calculate the number of phones sold
    phones_sold = this_year_production * sold_fraction

    # Calculate the number of phones left in the factory
    phones_left = this_year_production - phones_sold
    result = phones_left
    return result

print(solution())