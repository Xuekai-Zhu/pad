def solution():
    jeopardy_minutes = 20
    wheel_of_fortune_minutes = 2 * jeopardy_minutes

    # Calculate the total number of minutes of TV watched
    total_minutes = 2 * (jeopardy_minutes + wheel_of_fortune_minutes)

    # Convert minutes to hours
    total_hours = total_minutes / 60

    result = total_hours
    return result

print(solution())