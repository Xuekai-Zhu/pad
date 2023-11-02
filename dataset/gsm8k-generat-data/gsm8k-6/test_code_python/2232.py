def solution():
    # Calculate the total time Adam spent at school
    monday_time = 6 * 0.5  # 6 lessons of 30 minutes each
    tuesday_time = 3 * 1  # 3 lessons of 1 hour each
    wednesday_time = 2 * tuesday_time  # twice as much time as on Tuesday
    total_time = monday_time + tuesday_time + wednesday_time
    result = total_time
    return result

print(solution())