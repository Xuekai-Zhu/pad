def solution():
    """Brad's car broke down on an isolated road. At the time, Brad was traveling with Jim and Marcus. So, the three decided to push the car back into town, which was 10 miles away. For the first three miles, Brad steered as Jim and Marcus pushed at a speed of 6 miles per hour. Then, for the next 3 miles, Jim steered, as Brad and Marcus pushed at a speed of 3 miles per hour. For the last four miles, Marcus steered as Brad and Jim pushed at a speed of 8 miles per hour. How long did it take, in hours, to push the car back to town?"""
    distance_1 = 3
    distance_2 = 3
    distance_3 = 4
    speed_1 = 6
    speed_2 = 3
    speed_3 = 8
    time_1 = distance_1 / speed_1
    time_2 = distance_2 / speed_2
    time_3 = distance_3 / speed_3
    total_time = time_1 + time_2 + time_3
    result = total_time
    return result

print(solution())