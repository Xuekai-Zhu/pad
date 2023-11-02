def solution():
    starting_dogs = 10  # Guise ate 10 hot dogs on Monday
    dogs_tuesday = starting_dogs + 2  # Guise ate 2 more hot dogs on Tuesday
    dogs_wednesday = dogs_tuesday + 2  # Guise ate 2 more hot dogs on Wednesday

    # Calculate the total number of hot dogs Guise ate by Wednesday
    total_dogs = starting_dogs + dogs_tuesday + dogs_wednesday
    result = total_dogs
    return result

print(solution())