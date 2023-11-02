def solution():
    # Calculate the total number of balls inflated by both Alexia and Ermias
    total_balls = 20 + (20 + 5)  # Alexia inflates 20 balls, Ermias inflates 5 more than Alexia

    # Calculate the total time to inflate all the balls
    total_time = total_balls * 20  # it takes 20 minutes to inflate each ball

    result = total_time
    return result

print(solution())