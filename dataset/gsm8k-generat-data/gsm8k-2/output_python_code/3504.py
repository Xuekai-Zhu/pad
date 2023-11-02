def solution():
    """During a unit on probability, a teacher surveys her class asking her students two questions. The first question was whether they prefer dogs or cats, and the second question was whether they movies or video games. Of the 30 students in her class, 50% chose dogs and video games as their two answers, while 10% chose dogs and movies as their two answers. In total, how many students in this teacher's class prefer dogs over cats?"""
    total_students = 30
    dog_video_games = 0.5 * total_students
    dog_movies = 0.1 * total_students
    cat = 0.4 * total_students
    dog = dog_video_games + dog_movies
    cat = cat
    dog_over_cat = dog - cat
    result = dog_over_cat
    return result

print(solution())