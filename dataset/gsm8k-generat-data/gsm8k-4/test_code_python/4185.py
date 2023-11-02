def solution():
    """Emily bought 9 packs of candy necklaces to give her classmates at school for Valentine’s Day. Each pack had 8 candy necklaces in it. Emily opened one pack at a time. After her classmates took as many as they wanted, there were 40 candy necklaces left. How many packs did Emily open for her classmates?"""
    # Define the total number of candy necklaces and the number of necklaces in each pack
    total_necklaces = 9 * 8

    # Calculate the number of necklaces remaining after classmates took as many as they wanted
    remaining_necklaces = total_necklaces - 40

    # Calculate the number of packs opened by Emily for her classmates
    packs_opened = (total_necklaces - remaining_necklaces) / 8

    # Return the result
    result = packs_opened
    return result

print(solution())