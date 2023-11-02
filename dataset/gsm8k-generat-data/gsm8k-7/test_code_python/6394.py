def solution():
    total_balls = 100
    hole_percentage = 0.4
    overinflated_percentage = 0.2
    remaining_balls = (1 - hole_percentage) * total_balls

    # Calculate the number of balls that could not be inflated due to holes
    num_holed_balls = hole_percentage * total_balls

    # Calculate the number of balls that exploded due to overinflation
    num_exploded_balls = overinflated_percentage * remaining_balls

    # Calculate the number of balls that were successfully inflated and can be used
    num_inflated_balls = remaining_balls - num_exploded_balls - num_holed_balls

    result = num_inflated_balls
    return result

print(solution())