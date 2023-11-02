def solution():
    """There are 88 dogs in a park. 12 of the dogs are running. Half of them are playing with toys. A fourth of them are barking. How many dogs are not doing anything?"""
    # Define the total number of dogs
    total_dogs = 88

    # Calculate the number of dogs running
    running_dogs = 12

    # Calculate the number of dogs playing with toys
    toy_dogs = total_dogs / 2

    # Calculate the number of dogs barking
    barking_dogs = total_dogs / 4

    # Calculate the number of dogs not doing anything
    idle_dogs = total_dogs - running_dogs - toy_dogs - barking_dogs

    # return the result
    result = idle_dogs
    return result

print(solution())