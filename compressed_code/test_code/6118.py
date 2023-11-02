def solution():
    
    
    reggie_layups = 3
    reggie_ft = 2
    reggie_3pt = 1
    reggie_score = (reggie_layups * 1) + (reggie_ft * 2) + (reggie_3pt * 3)
    
    brother_layups = 0
    brother_ft = 0
    brother_3pt = 4
    brother_score = (brother_layups * 1) + (brother_ft * 2) + (brother_3pt * 3)
    
    point_diff = brother_score - reggie_score
    
    return point_diff

print(solution())