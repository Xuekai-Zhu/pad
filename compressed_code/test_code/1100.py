def solution():
    
    initial_dogs = 200
    moved_dogs = 100
    remaining_dogs = initial_dogs + moved_dogs
    dogs_for_adoption = 40
    remaining_dogs -= dogs_for_adoption
    adoptions = 60
    remaining_dogs -= adoptions
    result = remaining_dogs
    return result

print(solution())