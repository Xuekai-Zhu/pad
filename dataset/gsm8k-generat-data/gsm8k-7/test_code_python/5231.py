def solution():
    video_game_hours = 9
    study_hours = video_game_hours / 3
    grade_per_hour = 15

    # Calculate the total grade points earned from studying
    grade_points = grade_per_hour * study_hours

    # Add the total grade points earned to Jackson's starting grade of 0
    total_grade = 0 + grade_points
    result = total_grade
    return result

print(solution())