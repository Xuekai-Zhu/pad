def solution():
    """During a unit on probability, a teacher surveys her class asking her students two questions. The first question was whether they prefer dogs or cats, and the second question was whether they movies or video games. Of the 30 students in her class, 50% chose dogs and video games as their two answers, while 10% chose dogs and movies as their two answers. In total, how many students in this teacher's class prefer dogs over cats?"""
    total_students = 30
    dog_video_percent = 50
    dog_movie_percent = 10
    dog_percent = dog_video_percent + dog_movie_percent
    cat_percent = 100 - dog_percent
    dog_over_cat_percent = dog_percent - cat_percent
    dog_over_cat_students = (dog_over_cat_percent / 100) * total_students
    result = dog_over_cat_students
    
    return result

print(solution())