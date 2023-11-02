def solution():
    """Melissa bought 4 packs of tennis balls for $24 in total. Each pack contains 3 balls per pack. How much did it cost Melissa for each tennis ball?"""
    total_packs = 4
    total_cost = 24
    balls_per_pack = 3
    total_balls = total_packs * balls_per_pack
    cost_per_ball = total_cost / total_balls
    result = cost_per_ball
    return result

print(solution())