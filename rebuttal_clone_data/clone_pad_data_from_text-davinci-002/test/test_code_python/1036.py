def solution():
    soccer_balls = 20
    basketballs = soccer_balls + 5
    tennis_balls = 2 * soccer_balls
    baseballs = soccer_balls + 10
    volleyballs = 145 - (soccer_balls + basketballs + tennis_balls + baseballs)
    result = volleyballs
    return result

print(solution())