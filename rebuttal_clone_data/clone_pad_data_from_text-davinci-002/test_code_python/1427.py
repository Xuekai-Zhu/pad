def solution():
    starting_dogs = 200
    new_dogs = 100
    adopted_dogs = 40 + 60
    remaining_dogs = starting_dogs + new_dogs - adopted_dogs
    result = remaining_dogs
    return result

print(solution())