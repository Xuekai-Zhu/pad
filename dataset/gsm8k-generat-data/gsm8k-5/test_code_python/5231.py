def solution():
    video_game_hours = 9  # Jackson spends 9 hours playing video games
    study_hours = video_game_hours / 3  # Jackson spends 1/3 as much time studying
    grade_increase_per_hour = 15  # Jackson's grade increases by 15 points for every hour spent studying

    # Calculate Jackson's grade
    grade = study_hours * grade_increase_per_hour
    result = grade
    return result

print(solution())