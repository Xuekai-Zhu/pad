def solution():
    """There are some jelly beans in a jar. Three fourths of the jelly beans are red, and one quarter of the red jelly beans are coconut flavored. If 750 jelly beans are coconut flavored, how many jelly beans are there in the jar?"""
    coconut_flavored = 750
    red_jelly_beans = coconut_flavored / 0.25
    total_jelly_beans = red_jelly_beans / 0.75
    result = total_jelly_beans
    return result

print(solution())