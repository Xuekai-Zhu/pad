def solution():
    inflation_time = 20  # It takes 20 minutes to inflate one ball
    alexia_balls = 20  # Alexia inflates 20 balls
    ermias_balls = alexia_balls + 5  # Ermias inflates 5 more than Alexia

    # Calculate the total number of balls inflated
    total_balls = alexia_balls + ermias_balls

    # Calculate the total time taken to inflate all the balls
    total_time = inflation_time * total_balls
    result = total_time
    return result

print(solution())