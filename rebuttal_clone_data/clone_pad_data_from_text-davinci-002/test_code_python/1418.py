def solution():
    brushes = 20
    canvas = brushes * 3
    paint = 8
    liters = 5
    cost = brushes + canvas + (paint * liters)
    painting = 200
    profit = painting - cost
    result = profit
    return result

print(solution())