def solution():
    alexia_balls = 20
    ermias_balls = alexia_balls + 5
    inflation_time = 20

    # Calculate the total number of balls that they inflated
    total_balls = alexia_balls + ermias_balls

    # Calculate the total time it took to inflate all the balls
    total_time = total_balls * inflation_time
    result = total_time
    return result

print(solution())