def solution():
    
    alex_pens = 4
    jane_pens = 16
    for i in range(1, 4):
        alex_pens *= 2
    difference = alex_pens - jane_pens
    result = difference
    return result

print(solution())