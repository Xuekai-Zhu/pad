def solution():
    """Ginger likes to make cakes for every holiday for people. She has 2 children, each of whom she bakes a cake for on their birthdays, Christmas, Easter, and Halloween. She has a husband for whom she makes a cake on these same holidays, as well as on their anniversary and Valentine's Day. Lastly, she makes both her parents cakes as well, but only for their birthdays since they live far away. How many cakes does she make in 10 years?"""
    cakes_per_year = 2 * (4 + 3 + 2) + 1 * (4 + 2) + 2
    total_cakes = cakes_per_year * 10
    result = total_cakes
    return result

print(solution())