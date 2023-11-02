def solution():
    total_students = 30
    students_who_chose_dogs_and_video_games = total_students * 0.5
    students_who_chose_dogs_and_movies = total_students * 0.1
    result = students_who_chose_dogs_and_video_games + students_who_chose_dogs_and_movies
    return result

print(solution())