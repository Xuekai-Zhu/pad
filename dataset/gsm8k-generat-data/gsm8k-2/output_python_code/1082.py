def solution():
    """A factory produced televisions at a constant rate of 10 per day in a certain year. If they reduced the total production by 10 percent in the second year, calculate the total production of television by the factory in the second year."""
    year_1_production = 10 * 365
    year_2_production = year_1_production - (0.1 * year_1_production)
    result = year_2_production
    return result

print(solution())