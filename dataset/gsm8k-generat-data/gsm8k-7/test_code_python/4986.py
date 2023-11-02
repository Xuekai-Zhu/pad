def solution():
    flour_cost = 4
    sugar_cost = 2
    egg_cost = 0.5
    butter_cost = 2.5

    num_flour_cups = 2
    num_sugar_cups = 2
    num_eggs = 2
    num_butter_cups = 1

    total_cost = (num_flour_cups * flour_cost) + (num_sugar_cups * sugar_cost) + (num_eggs * egg_cost) + (num_butter_cups * butter_cost)

    num_slices = 6
    cost_per_slice = total_cost / num_slices

    num_slices_eaten = 2
    cost_eaten = num_slices_eaten * cost_per_slice

    result = cost_eaten
    return result

print(solution())