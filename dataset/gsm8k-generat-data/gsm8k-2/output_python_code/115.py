def solution():
    """There are some jelly beans in a jar. Three fourths of the jelly beans are red, and one quarter of the red jelly beans are coconut flavored. If 750 jelly beans are coconut flavored, how many jelly beans are there in the jar?"""
    coconut_red = 750
    red = coconut_red * 4
    total_jelly_beans = red / 3
    result = total_jelly_beans
    return result

print(solution())