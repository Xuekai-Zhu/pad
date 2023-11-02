def solution():
    """Los Angeles has 6 million people living in it. If half the population is women and 1/3 of the women work in retail, how many women work in retail in Los Angeles?"""
    # Calculate the number of women in Los Angeles
    women_population = 6_000_000 / 2

    # Calculate the number of women working in retail
    women_in_retail = women_population / 3

    # Display the result
    result = women_in_retail
    return result

print(solution())