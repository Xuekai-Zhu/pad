def solution():
    """Bonny just bought her 13th pair of shoes, which is 5 less than twice as many pairs of shoes as Becky owns.  Bobby has 3 times as many pairs of shoes as Becky has.  How many shoes does Bobby have?"""
    # Let's assume Becky owns x pairs of shoes.
    # Then, according to the problem, Bonny owns 2x-5 pairs of shoes.
    # And Bobby owns 3x pairs of shoes.
    # We also know that Bonny just bought her 13th pair of shoes,
    # which means that 2x-5 = 13.
    # Solving for x, we get x = 9.
    # Therefore, Bobby owns 3x = 27 pairs of shoes.

    # Calculate the number of shoes Bobby has
    bobby_shoes = 3 * 9

    # Return the result
    result = bobby_shoes
    return result

print(solution())