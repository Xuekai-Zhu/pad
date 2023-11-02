def solution():
    
    money_left = 20 - 8 - 4
    poster_cost = 4
    posters_bought = money_left // poster_cost
    result = posters_bought
    return result

print(solution())