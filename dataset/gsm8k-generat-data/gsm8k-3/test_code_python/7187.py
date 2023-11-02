def solution():
    """There are several cookies in the jar. Taking 1 cookie away would leave half as many in the jar as if 5 were added. How many cookies are in the jar?"""
    # Let's assume there are x cookies in the jar
    # If we take 1 cookie away, we are left with x-1 cookies
    # If we add 5 cookies, we have x+5 cookies
    # According to the problem, these two quantities are equal:

    x - 1 = (x + 5) / 2

    # To solve for x, we can simplify and solve for x:

    2x - 2 = x + 5
    x = 7

    # Therefore, there are 7 cookies in the jar
    result = 7
    return result

print(solution())