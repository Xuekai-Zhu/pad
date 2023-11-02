def solution():
    jeopardy_duration = 20 * 2
    wheel_of_fortune_duration = 2 * jeopardy_duration

    total_duration_minutes = jeopardy_duration * 2 + wheel_of_fortune_duration * 2
    total_duration_hours = total_duration_minutes / 60

    result = total_duration_hours
    return result

print(solution())