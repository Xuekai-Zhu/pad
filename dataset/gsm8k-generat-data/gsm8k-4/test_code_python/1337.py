def solution():
    """Bonny just bought her 13th pair of shoes, which is 5 less than twice as many pairs of shoes as Becky owns. Bobby has 3 times as many pairs of shoes as Becky has. How many shoes does Bobby have?"""
    # Let x be the number of shoes Becky owns
    # Then 2x - 5 is the number of shoes Bonny owns
    # And 3x is the number of shoes Bobby owns
    # We know that 2x - 5 = 13, so x = 9
    # Therefore, Bobby has 3 * 9 = 27 shoes

    bobby_shoes = 3 * 9
    result = bobby_shoes
    return result

print(solution())