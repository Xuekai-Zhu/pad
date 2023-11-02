def solution():
    """There are several cookies in the jar. Taking 1 cookie away would leave half as many in the jar as if 5 were added. How many cookies are in the jar?"""
    # Let's assume there are x cookies in the jar.
    # If we take 1 cookie away, there will be x-1 cookies left.
    # If we add 5 cookies, there will be x+5 cookies in the jar.
    # According to the problem, the following equation must be true:
    # x-1 = (x+5)/2
    # Solving for x, we get:
    x = (5/2) + 1
    result = x
    return result

print(solution())