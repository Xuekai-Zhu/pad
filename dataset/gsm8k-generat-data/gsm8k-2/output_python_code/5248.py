def solution():
    """Ginger likes to make cakes for every holiday for people. She has 2 children, each of whom she bakes a cake for on their birthdays, Christmas, Easter, and Halloween. She has a husband for whom she makes a cake on these same holidays, as well as on their anniversary and Valentine's Day. Lastly, she makes both her parents cakes as well, but only for their birthdays since they live far away. How many cakes does she make in 10 years?"""
    total_years = 10
    children_cakes = 2 * (5 + 1 + 1 + 1) * total_years
    husband_cakes = (5 + 2) * total_years
    parents_cakes = 2 * total_years
    total_cakes = children_cakes + husband_cakes + parents_cakes
    result = total_cakes
    return result

print(solution())