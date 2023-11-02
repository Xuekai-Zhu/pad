def solution():
    vaccine_percent = 1/3
    recovered_percent = 1/3
    vaccinated_and_recovered_percent = 1/6

    # Calculate the percent of the town that is only vaccinated
    only_vaccinated_percent = vaccine_percent - vaccinated_and_recovered_percent

    # Calculate the percent of the town that is only immune from previous COVID infection
    only_recovered_percent = recovered_percent - vaccinated_and_recovered_percent

    # Calculate the percent of the town that is immune in some way
    immune_percent = only_vaccinated_percent + only_recovered_percent + vaccinated_and_recovered_percent

    # Convert the decimal to a percentage
    immune_percent *= 100

    result = immune_percent
    return result

print(solution())