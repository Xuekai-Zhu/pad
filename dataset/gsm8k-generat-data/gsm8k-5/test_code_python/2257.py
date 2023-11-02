def solution():
    total_jelly_beans = 4000  # There are 4000 jelly beans in the jar
    red_jelly_beans = 0.75 * total_jelly_beans  # Three fourths of the jelly beans are red
    coconut_jelly_beans = 0.25 * red_jelly_beans  # One quarter of the red jelly beans are coconut flavored
    result = coconut_jelly_beans
    return result

print(solution())