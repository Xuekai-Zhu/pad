def solution():
    """Tom’s cat is 8 years old. His rabbit is half the age of his cat. His dog is three times as old as his rabbit. How old is the dog?"""
    # Define the age of the cat
    cat_age = 8

    # Calculate the age of the rabbit
    rabbit_age = cat_age / 2

    # Calculate the age of the dog
    dog_age = rabbit_age * 3

    # Return the age of the dog
    result = dog_age
    return result

print(solution())