def solution():
    
    total_beans = 572
    red_beans = total_beans // 4
    remaining_beans = total_beans - red_beans
    white_beans = remaining_beans // 3
    remaining_beans -= white_beans
    green_beans = remaining_beans // 2
    result = green_beans
    return result

print(solution())