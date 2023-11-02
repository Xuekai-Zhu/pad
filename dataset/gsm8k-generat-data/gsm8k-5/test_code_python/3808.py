def solution():
    # Calculate the number of flutes that got in
    flutes_in = 0.8 * 20

    # Calculate the number of clarinets that got in
    clarinets_in = 0.5 * 30

    # Calculate the number of trumpets that got in
    trumpets_in = (1/3) * 60

    # Calculate the number of pianists that got in
    pianists_in = (1/10) * 20

    # Calculate the total number of people in the band
    total_in_band = flutes_in + clarinets_in + trumpets_in + pianists_in
    result = total_in_band
    return result

print(solution())