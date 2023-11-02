def solution():
    # Calculate the number of students who prefer dogs and video games
    dogs_and_games = 0.5 * 30  # 50% of the class chose dogs and video games
    # Calculate the number of students who prefer dogs and movies
    dogs_and_movies = 0.1 * 30  # 10% of the class chose dogs and movies
    # Calculate the total number of students who prefer dogs
    total_dog_pref = dogs_and_games + dogs_and_movies
    result = total_dog_pref
    return result

print(solution())