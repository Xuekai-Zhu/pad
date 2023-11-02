def solution():
    """During a unit on probability, a teacher surveys her class asking her students two questions.  The first question was whether they prefer dogs or cats, and the second question was whether they movies or video games.  Of the 30 students in her class, 50% chose dogs and video games as their two answers, while 10% chose dogs and movies as their two answers.  In total, how many students in this teacher's class prefer dogs over cats?"""
    # Define the total number of students in the class
    total_students = 30

    # Determine the number of students who prefer dogs and video games
    dogs_video = total_students * 0.5

    # Determine the number of students who prefer dogs and movies
    dogs_movies = total_students * 0.1

    # Determine the number of students who prefer dogs over cats
    dogs_over_cats = dogs_video + dogs_movies

    # Display the number of students who prefer dogs over cats
    result = dogs_over_cats
    return result

print(solution())