def solution():
    """A paper company decides to operate their business more sustainably. They decide that for every tree they chop down, they want to plant three more. If the company chops down 200 trees in the first half of the year and 300 more trees in the second half of the year, how many more trees does the company need to plant?"""
    trees_chopped = 200 + 300
    trees_planted = trees_chopped * 3
    trees_needed = trees_planted - trees_chopped
    result = trees_needed
    return result

print(solution())