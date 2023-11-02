def solution():
    """Emily bought 9 packs of candy necklaces to give her classmates at school for Valentine’s Day. Each pack had 8 candy necklaces in it. Emily opened one pack at a time. After her classmates took as many as they wanted, there were 40 candy necklaces left. How many packs did Emily open for her classmates?"""
    # Define the number of candy necklaces in each pack
    PACK_SIZE = 8

    # Define the total number of packs that Emily bought
    total_packs = 9

    # Initialize the number of candy necklaces taken by Emily's classmates
    candy_taken = 0

    # Determine how many packs Emily opened for her classmates
    for i in range(total_packs):
        candy_taken += PACK_SIZE - 40
        if candy_taken >= total_packs * PACK_SIZE:
            packs_opened = i + 1
            break

    # Display the number of packs opened
    result = packs_opened
    return result

print(solution())