def solution():
    """Mary just held tryouts for the high school band. 80% of the 20 flutes got in, half the 30 clarinets got in, 1/3 of the 60 trumpets got in, and 1/10th of the 20 pianists got in. How many people are in the band total?"""
    # Define the number of flutes, clarinets, trumpets, and pianists
    flutes = 20
    clarinets = 30
    trumpets = 60
    pianists = 20

    # Calculate the number of each type of instrument that got in the band
    flutes_in = int(flutes * 0.8)
    clarinets_in = int(clarinets * 0.5)
    trumpets_in = int(trumpets * (1/3))
    pianists_in = int(pianists * 0.1)

    # Calculate the total number of people in the band
    total = flutes_in + clarinets_in + trumpets_in + pianists_in

    # Display the total number of people in the band
    result = total
    return result

print(solution())