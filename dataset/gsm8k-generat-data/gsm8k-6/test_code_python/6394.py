def solution():
    # Calculate the number of balls inflated successfully
    total_balls = 100
    failed_balls = 0.4 * total_balls  # 40 percent of the balls had holes in them
    remaining_balls = total_balls - failed_balls
    exploded_balls = 0.2 * remaining_balls  # 20 percent of the remaining balls were overinflated and exploded
    inflated_balls = remaining_balls - exploded_balls
    result = inflated_balls
    return result

print(solution())