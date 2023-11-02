def solution():
    num_country_cds = 23

    # Calculate the number of rock CDs Henry has
    num_rock_cds = (num_country_cds - 3) / 2

    # Calculate the total number of CDs in Henry's collection
    total_cds = num_country_cds + num_rock_cds + num_rock_cds / 2

    # Calculate the number of classical CDs in Henry's collection
    num_classical_cds = total_cds - num_country_cds - num_rock_cds
    result = num_classical_cds
    return result

print(solution())