def solution():
    # Calculate the total number of jelly beans needed to fill up the glasses
    jelly_beans_large = 50
    jelly_beans_small = jelly_beans_large // 2
    total_jelly_beans = (jelly_beans_large * 5) + (jelly_beans_small * 3)
    result = total_jelly_beans
    return result

print(solution())