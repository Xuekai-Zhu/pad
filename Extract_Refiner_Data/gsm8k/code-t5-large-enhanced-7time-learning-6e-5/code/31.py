def solution():
    
    # Define the total time played in minutes
    total_time = 40

    # Calculate the points scored in the first 20 minutes
    first_20_minutes_points = 4

    # Calculate the points scored in the second 20 minutes, which is 25% more than the first 20 minutes
    second_20_minutes_points = first_20_minutes_points * 1.25

    # Calculate the total points scored
    total_points = first_20_minutes_points + second_20_minutes_points

    # return the result
    result = total_points
    return result

print(solution())