def solution():
    # Calculate the time Adam spent at school on Monday
    monday_time = 6 * 0.5  # 6 lessons of 30 minutes each
    # Calculate the time Adam spent at school on Tuesday
    tuesday_time = 3 * 1  # 3 lessons of 1 hour each
    # Calculate the time Adam spent at school on Wednesday
    wednesday_time = 2 * tuesday_time  # Twice as much time as on Tuesday

    # Calculate the total time Adam spent at school in hours
    total_time = monday_time + tuesday_time + wednesday_time
    result = total_time
    return result

print(solution())