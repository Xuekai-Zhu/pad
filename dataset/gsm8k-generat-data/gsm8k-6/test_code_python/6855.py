def solution():
    # Let x be the number of hours it takes to bleach Cordelia's hair
    # Then the number of hours to dye her hair is 2x
    # The total time is 9 hours
    # Therefore:

    total_time = 9
    dye_time = 2*x
    bleach_time = x

    # The total time is the sum of the dye and bleach time:

    total_time = dye_time + bleach_time

    # Substituting in the equation gives:

    9 = 2*x + x

    # Solving for x yields:

    x = 3

    # Therefore, it will take Cordelia 3 hours to bleach her hair.

    result = x
    return result

print(solution())