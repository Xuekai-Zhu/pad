def solution():
    """A soccer ball takes twenty minutes to inflate. Alexia and Ermias are inflating balls, with Alexia inflating 20 balls and Ermias inflating 5 more balls than Alexia. Calculate the total time in minutes they took to inflate all the soccer balls."""
    time_per_ball = 20
    alexia_balls = 20
    ermias_balls = alexia_balls + 5
    total_balls = alexia_balls + ermias_balls
    total_time = total_balls * time_per_ball
    result = total_time
    return result

print(solution())