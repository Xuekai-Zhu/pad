def solution():
    
    total_jelly_beans = 100
    participating_children = int(40 * 0.8)
    jelly_beans_drawn = participating_children * 2
    remaining_jelly_beans = total_jelly_beans - jelly_beans_drawn
    result = remaining_jelly_beans
    return result

print(solution())