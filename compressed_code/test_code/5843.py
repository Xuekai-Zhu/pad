def solution():
    
    toast_cost = 1
    egg_cost = 3

    dale_toast = 2
    dale_eggs = 2
    dale_total = (dale_toast * toast_cost) + (dale_eggs * egg_cost)

    andrew_toast = 1
    andrew_eggs = 2
    andrew_total = (andrew_toast * toast_cost) + (andrew_eggs * egg_cost)

    total_cost = dale_total + andrew_total
    result = total_cost
    return result

print(solution())