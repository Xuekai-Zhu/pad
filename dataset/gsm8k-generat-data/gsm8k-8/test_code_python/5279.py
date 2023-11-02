def solution():
    # Calculate this year's production
    this_year_production = 2 * 5000

    # Calculate the number of phones sold
    phones_sold = 0.25 * this_year_production

    # Calculate the number of phones left in the factory
    phones_left = this_year_production - phones_sold
    result = phones_left
    return result

print(solution())