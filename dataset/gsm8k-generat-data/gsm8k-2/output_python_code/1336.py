def solution():
    """Bonny just bought her 13th pair of shoes, which is 5 less than twice as many pairs of shoes as Becky owns. Bobby has 3 times as many pairs of shoes as Becky has. How many shoes does Bobby have?"""
    bonny_shoes = 13
    becky_shoes = (bonny_shoes + 5) / 2
    bobby_shoes = 3 * becky_shoes
    result = bobby_shoes
    return result

print(solution())