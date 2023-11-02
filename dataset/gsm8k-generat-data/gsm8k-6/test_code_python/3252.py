def solution():
    # Calculate the total number of musicians in the orchestra
    orchestra_total = 11 + 12

    # Calculate the total number of musicians in the band
    band_total = orchestra_total * 2

    # Calculate the total number of musicians in the choir
    choir_total = 12 + 17

    # Calculate the total number of musicians in all three groups
    total_musicians = orchestra_total + band_total + choir_total
    result = total_musicians
    return result

print(solution())