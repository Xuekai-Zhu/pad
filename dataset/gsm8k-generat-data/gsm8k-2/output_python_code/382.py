def solution():
    """Anna baked 60 cupcakes. She gives away 4/5 of the cupcakes to her classmates. Of the remaining 1/5 of cupcakes, she eats 3 cupcakes. How many cupcakes does she have left?"""
    total_cupcakes = 60
    given_away_cupcakes = total_cupcakes * (4/5)
    remaining_cupcakes = total_cupcakes - given_away_cupcakes
    remaining_cupcakes -= 3
    result = remaining_cupcakes
    return result

print(solution())