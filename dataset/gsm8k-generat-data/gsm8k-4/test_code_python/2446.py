def solution():
    """Bob and Jim decide to skip rocks. Bob can skip a rock 12 times. Jim can skip a rock 15 times. If they each skipped 10 rocks how many total skips did they get?"""
    # Define Bob's and Jim's skips per rock
    bob_skips = 12
    jim_skips = 15

    # Define the number of rocks skipped by each person
    bob_rocks = 10
    jim_rocks = 10

    # Calculate the total number of skips
    total_skips = bob_skips * bob_rocks + jim_skips * jim_rocks

    # Return the result
    result = total_skips
    return result

print(solution())