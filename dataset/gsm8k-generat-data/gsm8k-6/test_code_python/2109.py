def solution():
    # Calculate the number of volcanoes that exploded in the first two months
    exploded_in_first_two_months = 0.2 * 200  

    # Calculate the number of volcanoes that haven't exploded yet
    remaining_volcanoes = 200 - exploded_in_first_two_months  

    # Calculate the number of volcanoes that exploded by half the year
    exploded_by_half_year = 0.4 * remaining_volcanoes  

    # Calculate the number of volcanoes that are still intact
    intact_volcanoes = remaining_volcanoes - exploded_by_half_year - 0.5 * remaining_volcanoes

    result = intact_volcanoes
    return result

print(solution())