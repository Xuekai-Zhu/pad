def solution():
    last_year_production = 5000  # Last year's production was 5000 phones
    this_year_production = 2 * last_year_production  # This year's production is twice last year's production
    quarter_production = this_year_production / 4  # A quarter of this year's production is sold
    phones_left = this_year_production - quarter_production  # Phones left in the factory
    result = phones_left
    return result

print(solution())