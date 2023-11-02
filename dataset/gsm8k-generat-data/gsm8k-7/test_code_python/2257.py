def solution():
    num_jelly_beans = 4000
    red_ratio = 3/4
    coconut_ratio = 1/4

    # Calculate the number of red jelly beans
    num_red_jelly_beans = num_jelly_beans * red_ratio

    # Calculate the number of coconut flavored jelly beans
    num_coconut_jelly_beans = num_red_jelly_beans * coconut_ratio
    result = num_coconut_jelly_beans
    return result

print(solution())