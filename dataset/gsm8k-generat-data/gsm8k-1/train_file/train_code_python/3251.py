def solution():
    """There are 11 males & 12 females in the orchestra and twice that number in the band. There are 12 males & 17 females in the choir. If each musician only participates in one group, how many musicians total are there in the orchestra, the band, and the choir?"""
    males_orchestra = 11
    females_orchestra = 12
    total_orchestra = males_orchestra + females_orchestra
    total_band = total_orchestra * 2
    males_choir = 12
    females_choir = 17
    total_choir = males_choir + females_choir
    result = total_orchestra + total_band + total_choir
    return result

print(solution())