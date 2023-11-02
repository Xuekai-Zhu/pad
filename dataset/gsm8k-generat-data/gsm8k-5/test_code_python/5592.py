def solution():
    total_cost = 24  # Melissa spent $24 in total
    num_packs = 4  # Melissa bought 4 packs of tennis balls
    balls_per_pack = 3  # Each pack contains 3 tennis balls

    # Calculate the total number of tennis balls Melissa bought
    total_balls = num_packs * balls_per_pack

    # Calculate the cost per tennis ball
    cost_per_ball = total_cost / total_balls
    result = cost_per_ball
    return result

print(solution())