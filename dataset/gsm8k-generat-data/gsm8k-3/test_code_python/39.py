def solution():
    """Anna goes trick-or-treating in a subdivision where she gets 14 pieces of candy per house. Her brother Billy goes trick-or-tricking in a neighboring subdivision where he gets 11 pieces of candy per house. If the first subdivision has 60 houses and the second subdivision has 75 houses, how many more pieces of candy does Anna get?"""
    # Calculate the total number of pieces of candy Anna gets
    anna_candy = 14 * 60

    # Calculate the total number of pieces of candy Billy gets
    billy_candy = 11 * 75

    # Calculate the difference in the number of pieces of candy Anna and Billy get
    candy_difference = anna_candy - billy_candy

    # Return the result
    result = candy_difference
    return result

print(solution())