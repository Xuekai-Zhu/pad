def solution():
    """An investor invested some money in 2 separate schemes: A and B. Scheme A will yield 30% of the capital within a year, and scheme B will yield 50% of the capital within a year. If he invested $300 in scheme A and $200 in B, how much more money will he have in scheme A than in B after a year, provided he does not withdraw anything?"""
    # Calculate the return on investment for scheme A after a year
    scheme_a_return = 300 * 0.3

    # Calculate the return on investment for scheme B after a year
    scheme_b_return = 200 * 0.5

    # Calculate the difference in returns between scheme A and scheme B
    return_difference = scheme_a_return - scheme_b_return

    # Display the difference in returns
    result = return_difference
    return result

print(solution())