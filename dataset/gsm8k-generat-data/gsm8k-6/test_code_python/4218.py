def solution():
    # Set up the equation to solve for Kirill's height
    # Let x be Kirill's height
    # Let y be his brother's height
    # then we have x + y = 112 and x = y -14
    # substitute x in second equation with the value obtained from the first equation and solve for y
    
    y = (112 + 14) / 2  # solve for y
    x = y - 14  # solve for x
    result = x
    return result

print(solution())