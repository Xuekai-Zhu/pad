def solution():
    # Calculate the number of volcanoes that exploded in the first two months
    first_two_months = 0.2 * 200
    remaining_volcanoes = 200 - first_two_months

    # Calculate the number of volcanoes that exploded by the half of the year
    half_of_year = 0.4 * remaining_volcanoes
    remaining_volcanoes -= half_of_year

    # Calculate the number of volcanoes that exploded at the end of the year
    end_of_year = 0.5 * remaining_volcanoes
    remaining_volcanoes -= end_of_year

    result = remaining_volcanoes
    return result

print(solution())