def solution():
    total_balls = 100  # Nova started with 100 soccer balls
    holes = 0.4 * total_balls  # 40% of the balls had holes and could not be inflated
    remaining_balls = total_balls - holes  # The remaining balls are the ones without holes
    overinflated = 0.2 * remaining_balls  # 20% of the remaining balls were overinflated and exploded
    inflated_balls = remaining_balls - overinflated  # The inflated balls are the ones that were not overinflated
    result = inflated_balls
    return result

print(solution())