def solution():
    """Anna goes trick-or-treating in a subdivision where she gets 14 pieces of candy per house. Her brother Billy goes trick-or-tricking in a neighboring subdivision where he gets 11 pieces of candy per house. If the first subdivision has 60 houses and the second subdivision has 75 houses, how many more pieces of candy does Anna get?"""
    # Define the number of houses in each subdivision
    anna_houses = 60
    billy_houses = 75

    # Define the number of pieces of candy per house in each subdivision
    anna_candy_per_house = 14
    billy_candy_per_house = 11

    # Calculate the total number of pieces of candy Anna and Billy get
    anna_total_candy = anna_houses * anna_candy_per_house
    billy_total_candy = billy_houses * billy_candy_per_house

    # Calculate the difference in the number of pieces of candy Anna and Billy get
    candy_difference = anna_total_candy - billy_total_candy

    # Return the result
    result = candy_difference
    return result

print(solution())