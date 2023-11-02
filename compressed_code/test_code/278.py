def solution():
    
    total_cupcakes = 60
    given_away_cupcakes = total_cupcakes * (4/5)
    remaining_cupcakes = total_cupcakes - given_away_cupcakes
    remaining_cupcakes -= 3
    result = remaining_cupcakes
    return result

print(solution())