def solution():
    """Brad's car broke down on an isolated road. At the time, Brad was traveling with Jim and Marcus. So, the three decided to push the car back into town, which was 10 miles away. 
    For the first three miles, Brad steered as Jim and Marcus pushed at a speed of 6 miles per hour. Then, for the next 3 miles, Jim steered, as Brad and Marcus pushed at a speed of 3 miles per hour. 
    For the last four miles, Marcus steered as Brad and Jim pushed at a speed of 8 miles per hour. How long did it take, in hours, to push the car back to town?"""
    distance = 10
    time_first_stage = 3 / 6
    time_second_stage = 3 / 3
    time_third_stage = 4 / 8
    total_time = time_first_stage + time_second_stage + time_third_stage
    result = total_time
    return result

print(solution())