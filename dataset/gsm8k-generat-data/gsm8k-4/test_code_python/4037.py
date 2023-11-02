def solution():
    """Susan has 21 cats and Bob has 3 cats. If Susan gives Robert 4 of her cats, how many more cats does Susan have than Bob?"""
    # Define the initial number of cats
    susan_cats = 21
    bob_cats = 3

    # Give away 4 cats from Susan to Bob
    susan_cats -= 4
    bob_cats += 4

    # Calculate the difference in the number of cats
    cat_difference = susan_cats - bob_cats

    # return the result
    result = cat_difference
    return result

print(solution())