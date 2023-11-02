def solution():
    roosevelt_points = [30, 15, 45]
    greendale_points = [(r - 10) for r in roosevelt_points]
    roosevelt_bonus = 50
    greendale_bonus = 0
    roosevelt_total = sum(roosevelt_points) + roosevelt_bonus
    greendale_total = sum(greendale_points) + greendale_bonus
    result = greendale_total
    
    return result

print(solution())