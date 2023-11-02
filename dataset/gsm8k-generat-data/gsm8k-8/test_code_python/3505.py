def solution():
    # Define the percentages of different preferences
    dogs_video = 0.5
    dogs_movies = 0.1

    # Calculate the percentage of students who prefer dogs over cats
    dogs_over_cats = dogs_video + dogs_movies - (dogs_video * dogs_movies)

    # Calculate the total number of students who prefer dogs over cats
    total_students = 30
    dogs_over_cats_count = round(dogs_over_cats * total_students)
    result = dogs_over_cats_count
    return result

print(solution())