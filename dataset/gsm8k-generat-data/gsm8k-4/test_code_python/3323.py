def solution():
    """Brad's car broke down on an isolated road. At the time, Brad was traveling with Jim and Marcus. So, the three decided to push the car back into town, which was 10 miles away. For the first three miles, Brad steered as Jim and Marcus pushed at a speed of 6 miles per hour. Then, for the next 3 miles, Jim steered, as Brad and Marcus pushed at a speed of 3 miles per hour. For the last four miles, Marcus steered as Brad and Jim pushed at a speed of 8 miles per hour. How long did it take, in hours, to push the car back to town?"""
    
    # Define the distances (in miles) for each leg of the journey
    distance_leg_1 = 3
    distance_leg_2 = 3
    distance_leg_3 = 4

    # Define the speeds (in miles per hour) for each leg of the journey
    speed_leg_1 = 6
    speed_leg_2 = 3
    speed_leg_3 = 8
  
    # Calculate the time (in hours) for each leg of the journey
    time_leg_1 = distance_leg_1 / speed_leg_1
    time_leg_2 = distance_leg_2 / speed_leg_2
    time_leg_3 = distance_leg_3 / speed_leg_3

    # Calculate the total time (in hours) for the entire journey
    total_time = time_leg_1 + time_leg_2 + time_leg_3

    # Return the result
    result = total_time
    return result

print(solution())