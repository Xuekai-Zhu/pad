def solution():
    """Danny brings 3 watermelons to his family picnic. He cuts each watermelon into 10 slices. His sister brings 1 watermelon to the family picnic, and she cuts the watermelon into 15 slices. How many watermelon slices are there in total at the picnic?"""
    # Define the number of watermelons and slices per watermelon
    DANNY_WATERMELONS = 3
    DANNY_SLICES = 10
    SISTER_WATERMELONS = 1
    SISTER_SLICES = 15

    # Calculate the total number of slices
    total_slices = (DANNY_WATERMELONS * DANNY_SLICES) + (SISTER_WATERMELONS * SISTER_SLICES)

    # Display the total number of slices
    result = total_slices
    return result

print(solution())