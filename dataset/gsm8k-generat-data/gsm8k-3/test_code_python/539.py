def solution():
    """A paper company decides to operate their business more sustainably. They decide that for every tree they chop down, they want to plant three more. If the company chops down 200 trees in the first half of the year and 300 more trees in the second half of the year, how many more trees does the company need to plant?"""
    # Calculate the number of trees that need to be planted for the first half of the year
    trees_planted_1 = 200 * 3

    # Calculate the number of trees that need to be planted for the second half of the year
    trees_planted_2 = 300 * 3

    # Calculate the total number of trees that need to be planted
    total_trees_planted = trees_planted_1 + trees_planted_2 - 500

    # Display the total number of trees that need to be planted
    result = total_trees_planted
    return result

print(solution())