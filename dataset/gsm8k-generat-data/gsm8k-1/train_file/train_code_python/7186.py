def solution():
    """There are several cookies in the jar. Taking 1 cookie away would leave half as many in the jar as if 5 were added. How many cookies are in the jar?"""
    # Let's use algebra to solve the problem
    # Let's say the original number of cookies is x
    # If we take one away, we are left with x-1 cookies
    # If we add 5, we have x+5 cookies
    # According to the problem, x-1 is half of x+5
    # So let's set up the equation:
    # x-1 = (x+5)/2
    
    # Let's solve for x:
    # 2(x-1) = x+5
    # 2x-2 = x+5
    # x = 7
    
    # Therefore, there were originally 7 cookies in the jar
    result = 7
    return result

print(solution())