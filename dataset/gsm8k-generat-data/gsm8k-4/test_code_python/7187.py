def solution():
    """There are several cookies in the jar. Taking 1 cookie away would leave half as many in the jar as if 5 were added. How many cookies are in the jar?"""
    # Let's assume there are 'x' cookies in the jar
    x = 0

    # Check all possible values of x until we find a solution that satisfies the condition
    while True:
        if (x-1)*2 == (x+5):
            # We have found a solution that satisfies the condition
            break
        # Move on to the next value of x
        x += 1

    # The solution is the value of x
    result = x
    return result

print(solution())