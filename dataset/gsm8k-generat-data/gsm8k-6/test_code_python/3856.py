def solution():
    # Calculate the number of caps collected in the first year
    first_year_caps = 3 * 12  # Lilith collects 3 caps per month in the first year

    # Calculate the number of caps collected in the second to fifth years
    remaining_years_caps = (5 * 12) * 5  # Lilith collects 5 caps per month after the first year, and has been collecting for 5 years

    # Calculate the number of Christmas caps received
    christmas_caps = 40 * 5  # Lilith receives 40 caps from friends and family each Christmas, and has had 5 Christmases

    # Calculate the number of lost caps
    lost_caps = 15 * 5  # Lilith estimates losing 15 caps each year, and has been collecting for 5 years

    # Calculate the total number of caps collected
    total_caps = first_year_caps + remaining_years_caps + christmas_caps - lost_caps
    result = total_caps
    return result

print(solution())