def solution():
    # Define the Disney Channel musical movies that feature Hades
    movies_with_hades = ["Descendants 3"]
    # Check if any of the movies in the list are Disney Channel musical movies
    disney_musicals = ["High School Musical", "Camp Rock", "Descendants"]
    for movie in movies_with_hades:
        if movie in disney_musicals:
            result = "yes"
            break
    else:
        result = "no"
    return result

print(solution())