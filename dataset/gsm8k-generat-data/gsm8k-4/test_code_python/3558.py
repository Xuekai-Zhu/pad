def solution():
    """Rocky boxed 190 fights in his career. 50 percent of his fights were knockouts, and 20 percent of the knockouts were in the first round. How many knockouts did Rocky have in the first round?"""
    # Calculate the number of fights that were knockouts
    knockouts = 190 * 0.5

    # Calculate the number of knockouts that occurred in the first round
    first_round_knockouts = knockouts * 0.2

    # Return the result
    result = first_round_knockouts
    return result

print(solution())