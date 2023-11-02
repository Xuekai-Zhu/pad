def solution():
    """There are 6 trees in Chris's yard. Ferdinand has half the number of trees that Chris has. Harry has 5 more than twice the number of trees that Ferdinand has. How many more trees are in Harry's yard than Ferdinand's yard?"""
    chris_trees = 6
    ferdinand_trees = chris_trees / 2
    harry_trees = 5 + (2 * ferdinand_trees)
    difference = harry_trees - ferdinand_trees
    result = difference
    return result

print(solution())