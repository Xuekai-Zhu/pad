def solution():
    """Mary just held tryouts for the high school band. 80% of the 20 flutes got in, half the 30 clarinets got in, 1/3 of the 60 trumpets got in, and 1/10th of the 20 pianists got in. How many people are in the band total?"""
    # Define the number of each instrument that got in
    flutes = 20 * 0.8
    clarinets = 30 * 0.5
    trumpets = 60 * (1/3)
    pianists = 20 * (1/10)

    # Calculate the total number of people in the band
    total_people = flutes + clarinets + trumpets + pianists

    result = total_people
    return result

print(solution())