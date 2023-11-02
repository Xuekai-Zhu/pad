def solution():
    """Mary sees three breeding balls with 8 snakes each and 6 additional pairs of snakes. How many snakes did she see total?"""
    # Define the number of snakes in each breeding ball
    snakes_per_ball = 8

    # Calculate the total number of snakes in the breeding balls
    total_snakes_in_balls = 3 * snakes_per_ball

    # Define the number of additional pairs of snakes
    additional_pairs = 6

    # Calculate the total number of additional snakes
    additional_snakes = additional_pairs * 2

    # Calculate the total number of snakes seen by Mary
    total_snakes_seen = total_snakes_in_balls + additional_snakes

    result = total_snakes_seen
    return result

print(solution())