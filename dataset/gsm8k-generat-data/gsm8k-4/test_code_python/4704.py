def solution():
    """John visits three different countries. He stays in the first country for 2 weeks and he spends twice as long in each of the other two countries. How much time does he spend on the trip?"""
    # Define the number of weeks John spends in each country
    country1_weeks = 2
    country2_weeks = country1_weeks * 2
    country3_weeks = country1_weeks * 2

    # Calculate the total number of weeks John spends on the trip
    total_weeks = country1_weeks + country2_weeks + country3_weeks

    # return the result
    result = total_weeks
    return result

print(solution())