def solution():
    """Jackson spends 9 hours playing video games and 1/3 that much time studying. If Jackson's grade starts at 0 points and increases by 15 points for every hour he spends studying, what is his grade?"""
    video_game_hours = 9
    study_hours = video_game_hours / 3
    grade_per_hour = 15
    grade = grade_per_hour * study_hours
    result = grade
    return result

print(solution())