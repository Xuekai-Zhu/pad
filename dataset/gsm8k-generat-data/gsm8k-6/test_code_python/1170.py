def solution():
    # Calculate the total time in minutes it will take Andy to get to school
    total_time = 30 + 3*4 + 10  # 30 minutes normal travel time, 3 minutes at 4 red lights, 10 minutes for construction
    # Calculate how many minutes late Andy will be
    late_time = total_time - (60-15)  # total time minus the time he has before school starts (60-15)
    result = late_time
    return result

print(solution())