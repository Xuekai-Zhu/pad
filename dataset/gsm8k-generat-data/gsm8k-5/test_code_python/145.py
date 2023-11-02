def solution():
    jeopardy_time = 20  # Each episode of Jeopardy is 20 minutes long
    wheel_of_fortune_time = 2 * jeopardy_time  # Each episode of Wheel of Fortune is twice as long as Jeopardy
    total_time = (2 * jeopardy_time) + (2 * wheel_of_fortune_time)  # James watched 2 episodes of each show
    hours_watched = total_time / 60  # Convert minutes to hours
    result = hours_watched
    return result

print(solution())