def solution():
    # Define the total number of dogs
    total_dogs = 88

    # Calculate the number of dogs running
    running_dogs = 12

    # Calculate the number of dogs playing with toys
    toy_dogs = total_dogs / 2

    # Calculate the number of dogs barking
    barking_dogs = total_dogs / 4

    # Calculate the number of dogs not doing anything
    not_doing_dogs = total_dogs - (running_dogs + toy_dogs + barking_dogs)

    result = not_doing_dogs
    return result

print(solution())