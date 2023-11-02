def solution():
    # Let's assume there are x cookies in the jar
    # If we take away 1, there will be x-1 cookies left
    # If we add 5, there will be x+5 cookies left
    # We know that x-1 is half of x+5, so we can set up an equation: 
    # x-1 = (x+5)/2 
    # Solving for x gives us:
    x = 9 # there are 9 cookies in the jar
    result = x
    return result

print(solution())