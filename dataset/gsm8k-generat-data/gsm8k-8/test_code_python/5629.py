def solution():
    # Define the fractions of the town that are vaccinated and immune from previous infection
    vaccinated_fraction = 1/3
    previous_infection_fraction = 1/3

    # Calculate the fraction of the town that is both vaccinated and has already had COVID
    vaccinated_and_infected_fraction = 1/6

    # Calculate the total fraction of the town that is immune
    total_immunity_fraction = vaccinated_fraction + previous_infection_fraction - vaccinated_and_infected_fraction

    # Convert the fraction to a percentage
    immune_percentage = total_immunity_fraction * 100
    result = immune_percentage
    return result

print(solution())