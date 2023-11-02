def solution():
    # Define the starting number of dogs
    starting_dogs = 80

    # Calculate the number of dogs adopted out
    adopted_dogs = starting_dogs * 0.4

    # Calculate the number of dogs returned
    returned_dogs = 5

    # Calculate the remaining number of dogs
    remaining_dogs = starting_dogs - adopted_dogs + returned_dogs

    result = remaining_dogs
    return result

print(solution())