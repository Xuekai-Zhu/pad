def solution():
    """There are 88 dogs in a park. 12 of the dogs are running. Half of them are playing with toys. A fourth of them are barking. How many dogs are not doing anything?"""
    # Define the total number of dogs and the number of dogs running
    total_dogs = 88
    running_dogs = 12

    # Calculate the number of dogs playing with toys and barking
    toy_dogs = total_dogs / 2
    bark_dogs = total_dogs / 4

    # Calculate the number of dogs doing nothing
    rest_dogs = total_dogs - running_dogs - toy_dogs - bark_dogs

    # Display the number of dogs doing nothing
    result = rest_dogs
    return result

print(solution())