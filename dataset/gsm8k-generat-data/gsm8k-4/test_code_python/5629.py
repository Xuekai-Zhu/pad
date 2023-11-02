def solution():
    """1/3 of the townspeople have received the full COVID vaccine. 1/3 are immune because they already recovered from COVID. If 1/6 of the townspeople are both vaccinated and already had COVID, what percent of the town is immune in some way?"""
    # Define the total number of townspeople
    total_population = 1

    # Calculate the number of townspeople who received the vaccine
    vaccinated_population = total_population * (1/3)

    # Calculate the number of townspeople who already recovered from COVID
    recovered_population = total_population * (1/3)

    # Calculate the number of townspeople who are both vaccinated and already had COVID
    vaccinated_and_recovered_population = total_population * (1/6)

    # Calculate the number of townspeople who are immune in some way (either vaccinated or recovered or both)
    total_immune_population = vaccinated_population + recovered_population - vaccinated_and_recovered_population

    # Calculate the percentage of townspeople who are immune in some way
    percent_immune_population = total_immune_population / total_population * 100

    # return the result
    result = percent_immune_population
    return result

print(solution())