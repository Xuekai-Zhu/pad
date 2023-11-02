def solution():
    # Calculate the total audience size
    audience_second_band = 2/3
    audience_first_band = 1/3
    total_audience_size = 1 / audience_second_band * (20 / 0.6) / 0.5

    # Calculate the number of people in each band
    second_band_size = total_audience_size * audience_second_band
    first_band_size = total_audience_size * audience_first_band

    # Calculate the total number of women at the concert
    women_second_band = 0.6 * 0.5 * second_band_size
    women_first_band = (1 - 0.6) * first_band_size
    total_women = women_second_band + women_first_band

    # Calculate the total number of men at the concert
    total_men = total_audience_size - total_women

    # Calculate the final result
    result = total_audience_size
    return result

print(solution())