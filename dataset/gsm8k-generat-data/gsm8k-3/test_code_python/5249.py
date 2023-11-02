def solution():
    """Ginger likes to make cakes for every holiday for people.  She has 2 children, each of whom she bakes a cake for on their birthdays, Christmas, Easter, and Halloween.  She has a husband for whom she makes a cake on these same holidays, as well as on their anniversary and Valentine's Day. Lastly, she makes both her parents cakes as well, but only for their birthdays since they live far away.  How many cakes does she make in 10 years?"""
    # Calculate the number of cakes she makes for each person
    child_cakes = 2 * (4 + 1 + 1 + 1)  # 2 children, each with 4 holiday cakes and 1 birthday cake
    husband_cakes = 7 + 1 + 1  # 7 holiday cakes, 1 anniversary cake, 1 Valentine's Day cake
    parent_cakes = 2  # 2 birthday cakes for her parents

    # Calculate the total number of cakes
    total_cakes = (child_cakes + husband_cakes + parent_cakes) * 10

    # Display the total number of cakes
    result = total_cakes
    return result

print(solution())