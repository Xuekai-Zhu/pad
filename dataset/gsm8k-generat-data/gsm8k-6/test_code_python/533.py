def solution():
    # Calculate the number of children who were allowed to draw jelly beans
    allowed_children = 0.8 * 40

    # Calculate the total number of jelly beans drawn by the children
    total_drawn = 2 * allowed_children

    # Calculate the number of jelly beans remaining in the bag
    remaining_jelly_beans = 100 - total_drawn
    result = remaining_jelly_beans
    return result

print(solution())