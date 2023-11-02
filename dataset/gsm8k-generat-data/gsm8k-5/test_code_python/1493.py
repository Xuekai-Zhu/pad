def solution():
    # Calculate the time taken for the first 100 miles
    time_first_leg = 1  # They drive the first 100 miles in 1 hour

    # Calculate the time taken for the remaining 300 miles
    speed = 60  # Assuming they maintain a constant speed of 60 miles per hour
    time_second_leg = 300 / speed 

    # Calculate the total time traveled
    total_time = time_first_leg + time_second_leg
    result = total_time
    return result

print(solution())