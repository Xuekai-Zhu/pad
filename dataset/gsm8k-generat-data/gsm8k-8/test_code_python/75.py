def solution():
    # Define the cost of each item
    toast_cost = 1
    egg_cost = 3

    # Calculate the cost of Dale's breakfast
    dale_toast = 2
    dale_eggs = 2
    dale_cost = dale_toast * toast_cost + dale_eggs * egg_cost

    # Calculate the cost of Andrew's breakfast
    andrew_toast = 1
    andrew_eggs = 2
    andrew_cost = andrew_toast * toast_cost + andrew_eggs * egg_cost

    # Calculate the total cost of their breakfast
    total_cost = dale_cost + andrew_cost
    result = total_cost
    return result

print(solution())