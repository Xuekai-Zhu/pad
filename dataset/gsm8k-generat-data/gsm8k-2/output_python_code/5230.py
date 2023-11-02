def solution():
    """Jackson spends 9 hours playing video games and 1/3 that much time studying. If Jackson's grade starts at 0 points and increases by 15 points for every hour he spends studying, what is his grade?"""
    video_game_time = 9
    study_time = video_game_time / 3
    grade_per_hour = 15
    total_grade = grade_per_hour * study_time
    result = total_grade
    return result

print(solution())