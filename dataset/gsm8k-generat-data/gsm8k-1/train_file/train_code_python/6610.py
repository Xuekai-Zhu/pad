def solution():
    """Mary sees three breeding balls with 8 snakes each and 6 additional pairs of snakes. How many snakes did she see total?"""
    snakes_per_breeding_ball = 8
    breeding_balls = 3
    additional_snake_pairs = 6
    total_snakes = (snakes_per_breeding_ball * breeding_balls) + (additional_snake_pairs * 2)
    result = total_snakes
    return result

print(solution())