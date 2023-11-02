def solution():
    """Jacob has half the number of shoes Edward has. Edward has 3 times the number of shoes Brian has. If Brian has 22 pairs of shoes, how many pairs of shoes do they have in total?"""
    brian_shoes = 22
    edward_shoes = 3 * brian_shoes
    jacob_shoes = edward_shoes / 2
    total_shoes = brian_shoes + edward_shoes + jacob_shoes
    result = total_shoes
    return result

print(solution())