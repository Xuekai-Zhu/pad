def solution():
    susan_cats = 21
    bob_cats = 3

    # Susan gives 4 cats to Bob
    susan_cats -= 4
    bob_cats += 4

    # Calculate the difference in cats between Susan and Bob
    cat_difference = susan_cats - bob_cats
    result = cat_difference
    return result

print(solution())