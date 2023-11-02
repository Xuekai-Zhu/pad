def solution():
    """Jackson spends 9 hours playing video games and 1/3 that much time studying. If Jackson's grade starts at 0 points and increases by 15 points for every hour he spends studying, what is his grade?"""
    # Define Jackson's time spent playing video games
    video_game_hours = 9

    # Calculate Jackson's time spent studying
    study_hours = video_game_hours / 3

    # Calculate Jackson's grade
    grade = study_hours * 15

    # Display Jackson's grade
    result = grade
    return result

print(solution())