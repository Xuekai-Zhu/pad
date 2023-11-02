def solution():
    """Daisy and Rose were enjoying their backyard pool with their dogs. If there are 24 legs/paws in the pool, how many dogs do Daisy and Rose have?"""
    # Define the number of legs per dog
    LEGS_PER_DOG = 4

    # Calculate the number of dogs based on the total number of legs
    total_legs = 24
    num_dogs = total_legs / LEGS_PER_DOG

    # Display the result
    result = num_dogs
    return result

print(solution())