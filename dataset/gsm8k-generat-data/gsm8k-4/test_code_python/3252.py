def solution():
    """There are 11 males & 12 females in the orchestra and twice that number in the band. There are 12 males & 17 females in the choir. If each musician only participates in one group, how many musicians total are there in the orchestra, the band, and the choir?"""
    # Calculate the number of musicians in the orchestra
    orchestra_males = 11
    orchestra_females = 12
    orchestra_total = orchestra_males + orchestra_females

    # Calculate the number of musicians in the band
    band_total = orchestra_total * 2

    # Calculate the number of musicians in the choir
    choir_males = 12
    choir_females = 17
    choir_total = choir_males + choir_females

    # Calculate the total number of musicians
    total_musicians = orchestra_total + band_total + choir_total

    # return the result
    result = total_musicians
    return result

print(solution())