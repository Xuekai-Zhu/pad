def solution():
    susan_cats = 21
    bob_cats = 3

    # Susan gives 4 cats to Bob
    susan_cats -= 4
    bob_cats += 4

    # Calculate how many more cats Susan has than Bob
    num_more_cats = susan_cats - bob_cats
    result = num_more_cats
    return result

print(solution())