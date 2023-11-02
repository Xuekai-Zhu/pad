def solution():
    outline_time = 30  # time spent outlining speech in minutes
    write_time = outline_time + 28  # time spent writing speech in minutes
    practice_time = write_time / 2  # time spent practicing speech in minutes
    total_time = outline_time + write_time + practice_time  # total time spent on speech in minutes
    result = total_time
    return result

print(solution())