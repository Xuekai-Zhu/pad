def solution():
    pieces_per_day = 3
    days = 72
    pie = 8
    slices_per_pie = pieces_per_day * days
    pizzas = slices_per_pie / pie
    result = pizzas
    return result

print(solution())