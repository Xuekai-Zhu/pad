def solution():
    # Calculate the total amount of time Mike spends playing video games in a week
    video_game_time = 4 * 0.5 * 3  # he plays for half as long as he watches TV, and plays 3 days a week
    # Calculate the total amount of time Mike spends watching TV in a week
    tv_time = 4 * 7 - video_game_time  # he watches TV for 4 hours a day, 7 days a week
    # Calculate the total amount of time Mike spends watching TV and playing video games in a week
    total_time = tv_time + video_game_time
    result = total_time
    return result

print(solution())