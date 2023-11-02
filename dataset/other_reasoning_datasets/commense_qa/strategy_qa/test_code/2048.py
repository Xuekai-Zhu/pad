def solution():
    movie_dogs = ["Golden Retriever", "Pit Bull"]
    associated_breeds = ["Greyhound"]
    overlap = [breed for breed in movie_dogs if breed in associated_breeds]
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())