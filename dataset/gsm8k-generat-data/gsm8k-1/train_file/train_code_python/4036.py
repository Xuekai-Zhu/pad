def solution():
    """Susan has 21 cats and Bob has 3 cats. If Susan gives Robert 4 of her cats, how many more cats does Susan have than Bob?"""
    susan_cats = 21
    bob_cats = 3
    susan_cats -= 4
    difference = susan_cats - bob_cats
    result = difference
    return result

print(solution())