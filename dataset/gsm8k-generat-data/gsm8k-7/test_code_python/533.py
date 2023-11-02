def solution():
    initial_num_jelly_beans = 100
    num_children = 40
    allowed_percentage = 0.8
    num_jelly_beans_drawn_per_child = 2

    # Calculate the number of children who were allowed to draw jelly beans
    num_allowed_children = int(num_children * allowed_percentage)

    # Calculate the total number of jelly beans drawn by the children
    total_jelly_beans_drawn = num_allowed_children * num_jelly_beans_drawn_per_child

    # Calculate the number of jelly beans remaining in the bag
    num_jelly_beans_remaining = initial_num_jelly_beans - total_jelly_beans_drawn
    result = num_jelly_beans_remaining
    return result

print(solution())