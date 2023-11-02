def solution():
    
    jeopardy_time = 20
    wheel_of_fortune_time = jeopardy_time * 2
    total_time = (jeopardy_time + wheel_of_fortune_time) * 2
    hours_watched = total_time / 60
    result = hours_watched
    return result

print(solution())