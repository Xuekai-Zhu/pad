def solution():
    initial_dogs = 80
    dogs_adopted = initial_dogs * 0.40
    dogs_returned = 5
    total_dogs = initial_dogs - dogs_adopted + dogs_returned
    result = total_dogs
    return result

print(solution())