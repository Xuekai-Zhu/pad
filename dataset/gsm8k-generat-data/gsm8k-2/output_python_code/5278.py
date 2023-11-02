def solution():
    """A phone factory makes twice as many phones as last year. Last year's production was 5000 phones. If a quarter of this year's production is sold, how many phones are left in the factory?"""
    last_year_production = 5000
    this_year_production = 2 * last_year_production
    sold_production = this_year_production / 4
    remaining_production = this_year_production - sold_production
    result = remaining_production
    return result

print(solution())