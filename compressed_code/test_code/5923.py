def solution():
    
    lisa_shirt_cost = 40
    lisa_jean_cost = lisa_shirt_cost / 2
    lisa_coat_cost = lisa_shirt_cost * 2
    carly_shirt_cost = lisa_shirt_cost / 4
    carly_jean_cost = lisa_jean_cost * 3
    carly_coat_cost = lisa_coat_cost / 4

    total_cost = lisa_shirt_cost + lisa_jean_cost + lisa_coat_cost + carly_shirt_cost + carly_jean_cost + carly_coat_cost
    result = total_cost

    return result

print(solution())