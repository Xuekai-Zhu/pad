def solution():
    """Susan has 21 cats and Bob has 3 cats. If Susan gives Robert 4 of her cats, how many more cats does Susan have than Bob?"""
    # Define the initial number of cats for Susan and Bob
    susan_cats = 21
    bob_cats = 3

    # Susan gives 4 cats to Bob
    susan_cats -= 4
    bob_cats += 4

    # Calculate the difference in the number of cats between Susan and Bob
    diff_cats = susan_cats - bob_cats

    # Display the difference in the number of cats
    result = diff_cats
    return result

print(solution())