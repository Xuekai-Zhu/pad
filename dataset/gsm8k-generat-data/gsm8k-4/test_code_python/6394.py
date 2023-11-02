def solution():
    """Of the 100 soccer balls that Nova went to inflate, 40 percent had holes in them and could not inflate, while 20% of the remaining balls were overinflated and exploded. How many balls were inflated successfully and could be used?"""
    # Define the initial number of soccer balls
    initial_balls = 100

    # Calculate the number of balls that had holes
    hole_balls = initial_balls * 0.4

    # Calculate the number of balls that were not inflated due to holes
    uninflated_balls = hole_balls

    # Calculate the number of balls that were not overinflated
    remaining_balls = initial_balls - uninflated_balls

    # Calculate the number of balls that exploded
    exploded_balls = remaining_balls * 0.2

    # Calculate the number of balls that were inflated successfully
    successful_balls = remaining_balls - exploded_balls

    # return the result
    result = successful_balls
    return result

print(solution())