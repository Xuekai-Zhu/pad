def solution():
    """Reggie and his brother are having a basketball shooting contest. They each get to take 10 shots. Layups are worth 1 point, free throws are worth 2 points, and anything further away is worth 3 points. Reggie makes 3 layups, two free throws, and one long shot. His brother only shoots long shots and makes 4 of them. How many points does Reggie lose by?"""
    
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