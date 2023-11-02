def solution():
    total_jelly_beans = 100
    participating_children = int(0.8 * 40)
    jelly_beans_drawn = participating_children * 2
    jelly_beans_remaining = total_jelly_beans - jelly_beans_drawn
    result = jelly_beans_remaining
    return result

print(solution())