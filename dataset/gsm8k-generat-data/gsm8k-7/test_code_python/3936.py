def solution():
    total_population = 6000000
    women_percentage = 0.5
    retail_percentage = 1/3

    # Calculate the total number of women in Los Angeles
    total_women = total_population * women_percentage

    # Calculate the number of women who work in retail
    women_in_retail = total_women * retail_percentage
    result = women_in_retail
    return result

print(solution())