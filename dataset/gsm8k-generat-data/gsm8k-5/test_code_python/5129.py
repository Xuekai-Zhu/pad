def solution():
    grapes = 100
    strawberries = (3/5)*grapes  # Karlee has 3/5 as many strawberries as grapes

    # Karlee gives 1/5 of each fruit to each friend
    karlee_left = grapes - (2*(1/5)*grapes)  # Karlee gives 1/5 of grapes to each friend
    karlee_left += strawberries - (2*(1/5)*strawberries)  # Karlee gives 1/5 of strawberries to each friend
    total_fruits = karlee_left + (2*(1/5)*grapes) + (2*(1/5)*strawberries)  # Karlee and her friends have a total of 100 grapes and 3/5 as many strawberries as grapes
    result = total_fruits
    return result

print(solution())