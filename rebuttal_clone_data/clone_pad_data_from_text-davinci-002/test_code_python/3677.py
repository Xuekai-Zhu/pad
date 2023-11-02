def solution():
    people_picking = 3
    pumpkins_grown = 83
    money_made = 96
    pumpkin_cost = people_picking * money_made
    pie_fillings = pumpkins_grown - pumpkin_cost
    result = pie_fillings
    return result

print(solution())