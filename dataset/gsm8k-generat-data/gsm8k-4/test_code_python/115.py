def solution():
    """There are some jelly beans in a jar. Three fourths of the jelly beans are red, and one quarter of the red jelly beans are coconut flavored. If 750 jelly beans are coconut flavored, how many jelly beans are there in the jar?"""
    # Let's assume there are 'x' jelly beans in the jar
    # 3/4 of the jelly beans in the jar are red
    red_jelly_beans = 3/4 * x

    # 1/4 of the red jelly beans are coconut flavored
    coconut_jelly_beans = 1/4 * red_jelly_beans

    # Given that there are 750 coconut flavored jelly beans
    # We can equate the above equation to 750 and solve for 'x'
    x = 750/(1/4 * 3/4)

    result = int(x)
    return result

print(solution())