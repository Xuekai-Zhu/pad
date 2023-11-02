def solution():
    # Calculate the cost of Dale's breakfast
    dale_toast = 2  # Dale had 2 slices of toast
    dale_eggs = 2 * 3  # Dale had 2 eggs at £3 each
    dale_cost = dale_toast + dale_eggs  # Calculate total cost of Dale's breakfast

    # Calculate the cost of Andrew's breakfast
    andrew_toast = 1  # Andrew had 1 slice of toast
    andrew_eggs = 2 * 3  # Andrew had 2 eggs at £3 each
    andrew_cost = andrew_toast + andrew_eggs  # Calculate total cost of Andrew's breakfast

    # Calculate the total cost of their breakfast
    total_cost = dale_cost + andrew_cost
    result = total_cost
    return result

print(solution())