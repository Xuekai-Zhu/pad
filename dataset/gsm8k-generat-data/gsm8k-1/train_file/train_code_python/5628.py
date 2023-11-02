def solution():
    """1/3 of the townspeople have received the full COVID vaccine. 1/3 are immune because they already recovered from COVID. If 1/6 of the townspeople are both vaccinated and already had COVID, what percent of the town is immune in some way?"""
    total_population = 1
    vaccinated_fraction = 1/3
    recovered_fraction = 1/3
    vaccinated_and_recovered_fraction = 1/6
    
    # Find the fraction of the population that is only vaccinated
    vaccinated_only_fraction = vaccinated_fraction - vaccinated_and_recovered_fraction
    
    # Find the fraction of the population that is only recovered
    recovered_only_fraction = recovered_fraction - vaccinated_and_recovered_fraction
    
    # Find the fraction of the population that is neither vaccinated nor recovered
    none_fraction = 1 - vaccinated_fraction - recovered_fraction - vaccinated_and_recovered_fraction
    
    # Find the total fraction of the population that is immune in some way (either vaccinated or recovered)
    immune_fraction = vaccinated_only_fraction + recovered_only_fraction + vaccinated_and_recovered_fraction
    
    # Convert the fraction to a percentage
    immune_percent = immune_fraction * 100
    
    result = immune_percent
    return result

print(solution())