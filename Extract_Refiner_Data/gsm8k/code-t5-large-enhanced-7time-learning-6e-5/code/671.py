def solution():
    
    # Define the number of dogs and the number of toys needed per dog
    num_dogs = 4
    toys_per_dog = 1

    # Calculate the total number of dogs and toys
    total_dogs = num_dogs + 8
    total_toys = (total_dogs * toys_per_dog) + (2 * num_dogs)

    # Subtract the number of dogs that were gone
    total_toys -= 3

    # return the result
    result = total_toys
    return result

print(solution())