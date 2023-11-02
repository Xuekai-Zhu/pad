def solution():
    """Joseph had 3 times as many notebooks as Martha. Martha decided she needed more notebooks and then bought 5 more for a total of 7 notebooks. How many more than Joseph does she now have?"""
    joseph_notebooks = 3
    martha_notebooks = 1
    martha_notebooks += 5
    difference = martha_notebooks - (joseph_notebooks * 3)
    result = difference
    return result

print(solution())