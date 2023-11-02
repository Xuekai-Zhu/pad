def solution():
    hours_per_video = 100
    average_speed = 1
    lila_speed = 2
    number_of_videos = 6
    lila_hours = number_of_videos * hours_per_video / lila_speed
    roger_hours = number_of_videos * hours_per_video / average_speed
    total_hours = lila_hours + roger_hours
    result = total_hours
    return result

print(solution())