def solution():
    
    jeopardy_time = 20 * 2
    wheel_of_fortune_time = jeopardy_time * 2
    total_time_in_minutes = jeopardy_time + wheel_of_fortune_time
    total_time_in_hours = total_time_in_minutes / 60
    result = total_time_in_hours
    return result

print(solution())