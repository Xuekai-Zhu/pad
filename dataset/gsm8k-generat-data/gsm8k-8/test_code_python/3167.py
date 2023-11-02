def solution():
    # Define the time it takes to inflate one soccer ball
    time_per_ball = 20

    # Define the number of soccer balls each person is inflating
    alexia_balls = 20
    ermias_balls = alexia_balls + 5

    # Calculate the total time it takes to inflate all the soccer balls
    total_time = (alexia_balls + ermias_balls) * time_per_ball
    result = total_time
    return result

print(solution())