def solution():
    """Ralph is going to practice playing tennis with a tennis ball machine that shoots out tennis balls for Ralph to hit. He loads up the machine with 175 tennis balls to start with. Out of the first 100 balls, he manages to hit 2/5 of them. Of the next 75 tennis balls, he manages to hit 1/3 of them. Out of all the tennis balls, how many did Ralph not hit?"""
    # Define the initial number of tennis balls and the proportion hit for the first 100 and next 75 balls
    total_balls = 175
    first_hit_proportion = 2/5
    next_hit_proportion = 1/3

    # Calculate the number of balls hit in the first 100
    first_hit_balls = int(total_balls * first_hit_proportion)

    # Calculate the number of balls not hit in the first 100
    first_not_hit_balls = 100 - first_hit_balls

    # Calculate the number of balls hit in the next 75
    next_hit_balls = int((total_balls - 100) * next_hit_proportion)

    # Calculate the number of balls not hit in the next 75
    next_not_hit_balls = 75 - next_hit_balls

    # Calculate the total number of balls not hit
    total_not_hit_balls = total_balls - first_hit_balls - next_hit_balls

    # return the result
    result = total_not_hit_balls
    return result

print(solution())