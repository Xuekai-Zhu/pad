def solution():
    total_time = 30 * 4  # The total time taken by all four runners is 30 seconds each
    total_time_last_three = 35 * 3  # The total time taken by the last three runners is 35 seconds each
    time_first_student = total_time - total_time_last_three  # The time taken by the first student is the difference between the total time and the time taken by the last three students

    result = time_first_student
    return result

print(solution())