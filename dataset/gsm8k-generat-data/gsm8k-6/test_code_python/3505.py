def solution():
    # Calculate the number of students who prefer dogs over cats
    total_dog_preference = 0
    dog_video_percentage = 50
    dog_movie_percentage = 10

    # Calculate the number of students who chose dogs and video games
    dog_video_students = (dog_video_percentage / 100) * 30

    # Calculate the number of students who chose dogs and movies
    dog_movie_students = (dog_movie_percentage / 100) * 30

    # Add the number of students who chose dogs and video games and dogs and movies
    total_dog_preference = dog_video_students + dog_movie_students

    result = total_dog_preference
    return result

print(solution())