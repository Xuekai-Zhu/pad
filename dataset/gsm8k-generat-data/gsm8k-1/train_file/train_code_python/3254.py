def solution():
    """April went to a concert that has two bands. 2/3 of the audience was there for the second band and 1/3 was there for the first band. 50% of the audience there for the second band is under the age of 30. Of this group, 60% are women and there are 20 men. How many people are at the concert?"""
    total_audience = 0
    second_band_audience = 0
    first_band_audience = 0
    second_band_under_30 = 0
    second_band_women_under_30 = 0
    
    # calculate total audience
    for i in range(1, 101):
        total_audience += i
    # calculate second band audience
    second_band_audience = total_audience * 2/3
    # calculate first band audience
    first_band_audience = total_audience * 1/3
    # calculate second band audience under 30
    second_band_under_30 = second_band_audience * 0.5
    # calculate second band women under 30
    second_band_women_under_30 = second_band_under_30 * 0.6
    
    # calculate total number of people at the concert
    total_people = second_band_women_under_30 * 2 + (second_band_under_30 - second_band_women_under_30) * 2 + (first_band_audience - second_band_under_30) * 2 + 20
    
    result = total_people
    return result

print(solution())