def solution():
    susan_cats = 21
    bob_cats = 3
    cats_given = 4

    # Susan gives 4 cats to Bob
    susan_cats -= cats_given
    bob_cats += cats_given

    # Calculate the difference in number of cats between Susan and Bob
    cat_difference = susan_cats - bob_cats
    result = cat_difference
    return result

print(solution())