def solution():
    # Calculate the number of people who got into the band for each instrument
    flutes = 0.8 * 20
    clarinets = 0.5 * 30
    trumpets = (1/3) * 60
    pianists = (1/10) * 20

    # Calculate the total number of people in the band
    total_people = flutes + clarinets + trumpets + pianists
    result = total_people
    return result

print(solution())