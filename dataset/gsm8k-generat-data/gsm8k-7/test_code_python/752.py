def solution():
    area = 100
    
    # Find the width of the rectangle by solving for w in the equation A = lw and substituting l = 4w
    width = area / 4
    
    # Find the length of the rectangle using the equation l = 4w
    length = 4 * width
    
    result = length
    return result

print(solution())