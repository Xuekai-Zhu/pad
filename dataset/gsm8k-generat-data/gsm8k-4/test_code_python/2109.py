def solution():
    """A mountain range has 200 active volcanoes. In a particular year, 20% of the volcanoes exploded in the first two months, 40% of the remaining exploded by the half of the year, and at the end of the year, another 50% of the volcanoes that hadn't already erupted also exploded. How many mountains are still intact at the end of the year?"""
    # Define the initial number of active volcanoes
    active_volcanoes = 200

    # Calculate the number of volcanoes that exploded in the first two months
    exploded_first_two_months = active_volcanoes * 0.2

    # Calculate the remaining number of active volcanoes
    remaining_volcanoes = active_volcanoes - exploded_first_two_months

    # Calculate the number of volcanoes that exploded by the half of the year
    exploded_half_of_the_year = remaining_volcanoes * 0.4

    # Calculate the remaining number of active volcanoes
    remaining_volcanoes -= exploded_half_of_the_year

    # Calculate the number of volcanoes that exploded by the end of the year
    exploded_end_of_year = remaining_volcanoes * 0.5

    # Calculate the number of intact mountains at the end of the year
    result = remaining_volcanoes - exploded_end_of_year
    return result

print(solution())