def solution():
    """A soccer ball takes twenty minutes to inflate. Alexia and Ermias are inflating balls, with Alexia inflating 20 balls and Ermias inflating 5 more balls than Alexia. Calculate the total time in minutes they took to inflate all the soccer balls."""
    # Define the time it takes to inflate one ball
    time_per_ball = 20

    # Define the number of balls Alexia inflates
    alexia_balls = 20

    # Define the number of balls Ermias inflates
    ermias_balls = alexia_balls + 5

    # Calculate the total number of balls
    total_balls = alexia_balls + ermias_balls

    # Calculate the total time it takes to inflate all the balls
    total_time = total_balls * time_per_ball

    result = total_time
    return result

print(solution())