def solution():
    # Calculate the number of jelly beans Thomas takes
    thomas_jelly_beans = 0.1 * 200  # Thomas takes 10% of the jelly beans

    # Calculate the remaining jelly beans after Thomas takes his share
    remaining_jelly_beans = 200 - thomas_jelly_beans

    # Calculate the total ratio of jelly beans to be shared by Barry and Emmanuel
    total_ratio = 4 + 5

    # Calculate the fraction of jelly beans that Emmanuel gets
    emmanuel_fraction = 5 / total_ratio

    # Calculate the number of jelly beans that Emmanuel gets
    emmanuel_jelly_beans = emmanuel_fraction * remaining_jelly_beans

    result = emmanuel_jelly_beans
    return result

print(solution())