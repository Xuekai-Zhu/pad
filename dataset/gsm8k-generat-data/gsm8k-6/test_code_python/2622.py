def solution():
    # Find the number of jelly beans Sedrich has
    sedrich_jelly_beans = 17 + 4

    # Find the sum of Napoleon and Sedrich's jelly beans
    sum_jelly_beans = 17 + sedrich_jelly_beans

    # Find the number of jelly beans Mikey has
    mikey_jelly_beans = (2 * sum_jelly_beans) / 4

    result = mikey_jelly_beans
    return result

print(solution())