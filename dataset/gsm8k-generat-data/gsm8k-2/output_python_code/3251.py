def solution():
    """There are 11 males & 12 females in the orchestra and twice that number in the band. There are 12 males & 17 females in the choir. If each musician only participates in one group, how many musicians total are there in the orchestra, the band, and the choir?"""
    orchestra_males = 11
    orchestra_females = 12
    band_males = 2 * orchestra_males
    band_females = 2 * orchestra_females
    choir_males = 12
    choir_females = 17
    total_musicians = orchestra_males + orchestra_females + band_males + band_females + choir_males + choir_females
    result = total_musicians
    return result

print(solution())