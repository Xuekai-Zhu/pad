def solution():
    total_jelly_beans = 100
    total_children = 40
    children_allowed = total_children * 0.8
    jelly_beans_taken = children_allowed * 2
    jelly_beans_left = total_jelly_beans - jelly_beans_taken
    result = jelly_beans_left
    return result

print(solution())