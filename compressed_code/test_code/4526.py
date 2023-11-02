def solution():
    
    
    g = 20 
    r = 7 + 3*g
    b = g - 5
    total_fruits = r + g + b

    while total_fruits != 102:
        if total_fruits < 102:
            g += 1
        else:
            g -= 1

        r = 7 + 3*g
        b = g - 5
        total_fruits = r + g + b

    result = r
    return result

print(solution())