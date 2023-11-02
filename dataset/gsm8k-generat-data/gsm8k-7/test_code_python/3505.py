def solution():
    num_students = 30
    dogs_video_games = 0.5 * num_students
    dogs_movies = 0.1 * num_students
    dogs_only = dogs_video_games - dogs_movies
    cats_only = (num_students - dogs_only) / 2
    result = dogs_only + cats_only
    return result

print(solution())