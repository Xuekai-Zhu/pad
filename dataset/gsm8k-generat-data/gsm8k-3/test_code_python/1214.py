def solution():
    """Adlai has 2 dogs and 1 chicken. How many animal legs are there in all?"""
    # Define the number of legs per dog and chicken
    LEGS_PER_DOG = 4
    LEGS_PER_CHICKEN = 2

    # Define the number of dogs and chicken
    num_dogs = 2
    num_chicken = 1

    # Calculate the total number of legs
    total_legs = (num_dogs * LEGS_PER_DOG) + (num_chicken * LEGS_PER_CHICKEN)

    result = total_legs
    return result

print(solution())