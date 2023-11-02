def solution():
    toast_cost = 1
    egg_cost = 3

    dale_toast = 2
    dale_eggs = 2

    andrew_toast = 1
    andrew_eggs = 2

    # Calculate the total cost of Dale's order
    dale_cost = (dale_toast * toast_cost) + (dale_eggs * egg_cost)

    # Calculate the total cost of Andrew's order
    andrew_cost = (andrew_toast * toast_cost) + (andrew_eggs * egg_cost)

    # Calculate the total cost of both orders
    total_cost = dale_cost + andrew_cost
    result = total_cost
    return result

print(solution())