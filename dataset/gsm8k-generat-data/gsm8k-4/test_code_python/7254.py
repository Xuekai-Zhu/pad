def solution():
    """In Henry's collection of music CDs, he has 3 more country CDs than rock CDs but twice as many rock CDs as classical CDs. If he has 23 country CDs, how many classical CDs make up his collection?"""
    # Define the number of country CDs
    country_cds = 23

    # Calculate the number of rock CDs
    rock_cds = (country_cds - 3) / 2

    # Calculate the number of classical CDs
    classical_cds = rock_cds / 2

    result = classical_cds
    return result

print(solution())