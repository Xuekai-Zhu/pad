def solution():
    """Jackson spends 9 hours playing video games and 1/3 that much time studying. If Jackson's grade starts at 0 points and increases by 15 points for every hour he spends studying, what is his grade?"""
    # Define the number of hours spent playing video games
    video_game_hours = 9

    # Calculate the number of hours spent studying
    study_hours = video_game_hours / 3

    # Calculate the total number of points earned
    points = study_hours * 15

    # return the result
    result = points
    return result

print(solution())