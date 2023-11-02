def solution():
    """A paper company decides to operate their business more sustainably. They decide that for every tree they chop down, they want to plant three more. If the company chops down 200 trees in the first half of the year and 300 more trees in the second half of the year, how many more trees does the company need to plant?"""
    # Define the number of trees chopped down
    trees_chopped = 200 + 300

    # Calculate the number of trees that need to be planted
    trees_planted = trees_chopped * 3

    # Calculate the additional trees that need to be planted to reach the company's goal
    additional_trees_planted = trees_planted - trees_chopped

    # return the result
    result = additional_trees_planted
    return result

print(solution())