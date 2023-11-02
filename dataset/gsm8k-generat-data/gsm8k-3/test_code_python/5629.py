def solution():
    """1/3 of the townspeople have received the full COVID vaccine. 1/3 are immune because they already recovered from COVID.
    If 1/6 of the townspeople are both vaccinated and already had COVID, what percent of the town is immune in some way?"""
    
    # Define the fractions of vaccinated, recovered, and both vaccinated and recovered townspeople
    vaccinated_fraction = 1/3
    recovered_fraction = 1/3
    vaccinated_and_recovered_fraction = 1/6
    
    # Calculate the fraction of people who are immune in some way
    immune_fraction = vaccinated_fraction + recovered_fraction - vaccinated_and_recovered_fraction
    
    # Convert the fraction to a percentage
    immune_percentage = immune_fraction * 100
    
    # Display the percentage of people who are immune in some way
    result = immune_percentage
    return result

print(solution())