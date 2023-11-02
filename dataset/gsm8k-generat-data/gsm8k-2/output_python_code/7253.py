def solution():
    """In Henry's collection of music CDs, he has 3 more country CDs than rock CDs but twice as many rock CDs as classical CDs. If he has 23 country CDs, how many classical CDs make up his collection?"""
    country_cds = 23
    rock_cds = (country_cds - 3) / 2
    classical_cds = rock_cds / 2
    total_cds = country_cds + rock_cds + classical_cds
    result = classical_cds
    return result

print(solution())