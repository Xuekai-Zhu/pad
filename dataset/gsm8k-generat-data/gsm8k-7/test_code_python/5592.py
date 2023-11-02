def solution():
    num_packs = 4
    total_cost = 24
    balls_per_pack = 3

    # Calculate the total number of tennis balls Melissa bought
    total_balls = num_packs * balls_per_pack

    # Calculate the cost per tennis ball
    cost_per_ball = total_cost / total_balls
    result = cost_per_ball
    return result

print(solution())