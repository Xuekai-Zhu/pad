def solution():
    # Define the number of country CDs and the relation between country and rock CDs
    country_cds = 23
    rock_cds = 2 * classical_cds
    country_to_rock = rock_cds - (country_cds + 3)

    # Calculate the number of classical CDs
    classical_cds = country_to_rock / 3
    result = classical_cds
    return result

print(solution())