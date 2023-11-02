def solution():
    breeding_balls = 3
    snakes_per_breeding_ball = 8
    additional_pairs = 6

    # Calculate the total number of snakes from breeding balls
    breeding_ball_snakes = breeding_balls * snakes_per_breeding_ball

    # Calculate the total number of snakes from additional pairs
    additional_snakes = additional_pairs * 2

    # Calculate the total number of snakes that Mary saw
    total_snakes = breeding_ball_snakes + additional_snakes
    result = total_snakes
    return result

print(solution())