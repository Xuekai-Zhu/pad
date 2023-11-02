def solution():
    """April went to a concert that has two bands. 2/3 of the audience was there for the second band and 1/3 was there for the first band. 50% of the audience there for the second band is under the age of 30. Of this group, 60% are women and there are 20 men. How many people are at the concert?"""
    total_audience = 0
    first_band_audience = total_audience // 3
    second_band_audience = 2 * (total_audience // 3)
    second_band_under_30 = 0.5 * second_band_audience
    second_band_over_30 = second_band_audience - second_band_under_30
    second_band_under_30_women = 0.6 * second_band_under_30
    second_band_under_30_men = 0.4 * second_band_under_30
    total_men = second_band_under_30_men + 20
    total_women = second_band_under_30_women + (second_band_over_30 * 0.5)
    total_audience = first_band_audience + second_band_audience
    result = total_audience
    return result

print(solution())