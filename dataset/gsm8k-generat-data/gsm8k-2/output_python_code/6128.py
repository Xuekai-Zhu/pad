def solution():
    """Scott has 7 pairs of shoes. Anthony has 3 times as many pairs of shoes as Scott, and Jim has 2 less pairs than Anthony. How many more pairs of shoes does Anthony have compared to Jim?"""
    scott_shoes = 7
    anthony_shoes = 3 * scott_shoes
    jim_shoes = anthony_shoes - 2
    diff = anthony_shoes - jim_shoes
    result = diff
    return result

print(solution())