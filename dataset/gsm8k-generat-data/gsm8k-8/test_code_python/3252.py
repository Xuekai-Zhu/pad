def solution():
    # Calculate the total number of musicians in the orchestra
    orchestra_total = 11 + 12

    # Calculate the total number of musicians in the band
    band_total = 2 * (orchestra_total)

    # Calculate the total number of musicians in the choir
    choir_total = 12 + 17

    # Calculate the total number of musicians
    total_musicians = orchestra_total + band_total + choir_total
    result = total_musicians
    return result

print(solution())