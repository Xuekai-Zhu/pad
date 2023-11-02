def solution():
    """Danny brings 3 watermelons to his family picnic. He cuts each watermelon into 10 slices. His sister brings 1 watermelon to the family picnic, and she cuts the watermelon into 15 slices. How many watermelon slices are there in total at the picnic?"""
    # Calculate the number of watermelon slices from Danny's watermelons
    danny_slices = 3 * 10

    # Calculate the number of watermelon slices from his sister's watermelon
    sister_slices = 1 * 15

    # Calculate the total number of watermelon slices at the picnic
    total_slices = danny_slices + sister_slices

    result = total_slices
    return result

print(solution())