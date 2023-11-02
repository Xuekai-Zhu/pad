def solution():
    """April went to a concert that has two bands. 2/3 of the audience was there for the second band and 1/3 was there for the first band. 50% of the audience there for the second band is under the age of 30. Of this group, 60% are women and there are 20 men. How many people are at the concert?"""
    # Define the fraction of the audience for each band
    band1_fraction = 1/3
    band2_fraction = 2/3

    # Calculate the number of people in the audience for each band
    total_audience = None 
    band2_audience = band2_fraction * total_audience
    band1_audience = band1_fraction * total_audience

    # Calculate the number of people under 30 at the concert for the second band
    band2_under30 = band2_audience * 0.5
    band2_women_under30 = band2_under30 * 0.6
    band2_men_under30 = 20
    band2_total_under30 = band2_women_under30 + band2_men_under30

    # Calculate the total number of women at the concert for the second band
    band2_women = 2 * band2_women_under30

    # Calculate the total number of men at the concert for the second band
    band2_men = 2 * band2_men_under30

    # Calculate the total number of people at the concert
    total_audience = band1_audience + band2_audience
    total_women = band2_women
    total_men = band1_audience/3 + band2_men

    result = total_audience
    return result

print(solution())