def solution():
    
    total_packs = 4
    total_cost = 24
    balls_per_pack = 3
    total_balls = total_packs * balls_per_pack
    cost_per_ball = total_cost / total_balls
    result = cost_per_ball
    return result

print(solution())