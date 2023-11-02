def solution():
    flour_cost = 4
    sugar_cost = 2
    egg_cost = .5
    butter_cost = 2.5
    cake_cost = flour_cost + sugar_cost + egg_cost + butter_cost
    slices_per_cake = 6
    cake_slice_cost = cake_cost / slices_per_cake
    result = cake_slice_cost
    return result

print(solution())