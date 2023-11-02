def solution():
    """There are 11 males & 12 females in the orchestra and twice that number in the band. There are 12 males & 17 females in the choir. If each musician only participates in one group, how many musicians total are there in the orchestra, the band, and the choir?"""
    # Define the number of males and females in the orchestra
    orchestra_males = 11
    orchestra_females = 12

    # Define the number of musicians in the orchestra
    orchestra_total = orchestra_males + orchestra_females

    # Define the number of musicians in the band (twice the number in the orchestra)
    band_total = orchestra_total * 2

    # Define the number of males and females in the choir
    choir_males = 12
    choir_females = 17

    # Define the number of musicians in the choir
    choir_total = choir_males + choir_females

    # Calculate the total number of musicians
    total_musicians = orchestra_total + band_total + choir_total

    # Display the total number of musicians
    result = total_musicians
    return result

print(solution())