def solution():
    # Calculate the total number of snakes in the breeding balls
    breeding_balls_snakes = 3 * 8  # Three breeding balls with 8 snakes each

    # Calculate the total number of snakes from the additional pairs
    additional_pairs_snakes = 6 * 2  # Six pairs of snakes, each with two snakes

    # Calculate the total number of snakes Mary saw
    total_snakes = breeding_balls_snakes + additional_pairs_snakes
    result = total_snakes
    return result

print(solution())