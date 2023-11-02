def solution():
    
    initial_dogs = 80
    adopted_dogs = int(initial_dogs * 0.4)
    returned_dogs = 5
    remaining_dogs = initial_dogs - adopted_dogs + returned_dogs
    result = remaining_dogs
    return result

print(solution())