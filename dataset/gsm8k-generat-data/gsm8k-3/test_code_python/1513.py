def solution():
    """Tom’s cat is 8 years old.  His rabbit is half the age of his cat.  His dog is three times as old as his rabbit.  How old is the dog?"""
    # Define the age of Tom's cat
    cat_age = 8

    # Calculate the age of Tom's rabbit
    rabbit_age = cat_age / 2

    # Calculate the age of Tom's dog
    dog_age = rabbit_age * 3

    # Display the age of Tom's dog
    result = dog_age
    return result

print(solution())