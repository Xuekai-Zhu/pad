def solution():
    # Let's assume there are a total of 100 people at the concert
    total_audience = 100

    # 1/3 of the audience is there for the first band
    first_band_audience = total_audience / 3

    # 2/3 of the audience is there for the second band
    second_band_audience = (2 / 3) * total_audience

    # 50% of the audience there for the second band is under the age of 30
    young_second_band_audience = 0.5 * second_band_audience

    # Of this group, 60% are women and there are 20 men
    num_women = 0.6 * young_second_band_audience
    num_men = 20
    num_young_second_band_audience = num_women + num_men

    # Calculate the total number of people at the concert
    total_audience = first_band_audience + second_band_audience

    # Update the number of people in the second band audience
    second_band_audience = num_young_second_band_audience / 0.5

    # Calculate the total number of people at the concert
    total_audience = first_band_audience + second_band_audience

    result = total_audience
    return result

print(solution())