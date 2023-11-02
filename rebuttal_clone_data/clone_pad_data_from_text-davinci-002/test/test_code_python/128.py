def solution():
    
    packs_red = 7
    packs_yellow = 6
    bouncy_balls_per_pack = 18
    total_red_bouncy_balls = packs_red * bouncy_balls_per_pack
    total_yellow_bouncy_balls = packs_yellow * bouncy_balls_per_pack
    difference = total_red_bouncy_balls - total_yellow_bouncy_balls
    result = difference
    return result

print(solution())