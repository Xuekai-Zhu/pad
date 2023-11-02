def solution():
    """There are some jelly beans in a jar. Three fourths of the jelly beans are red, and one quarter of the red jelly beans are coconut flavored. If 750 jelly beans are coconut flavored, how many jelly beans are there in the jar?"""
    # Let's assume there are x jelly beans in the jar
    # 3/4 of them are red, so the number of red jelly beans is 3/4 * x
    # 1/4 of the red jelly beans are coconut flavored, so the number of coconut flavored jelly beans is 1/4 * 3/4 * x = 3/16 * x
    # We know that there are 750 coconut flavored jelly beans, so we can set up the equation:
    # 3/16 * x = 750
    # Solving for x:
    x = 750 * (16/3)
    result = int(x)
    return result

print(solution())