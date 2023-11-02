def solution():
    """Adlai has 2 dogs and 1 chicken. How many animal legs are there in all?"""
    # Define the number of legs for a dog and a chicken
    legs_per_dog = 4
    legs_per_chicken = 2

    # Calculate the total number of legs
    total_legs = (2 * legs_per_dog) + (1 * legs_per_chicken)
    
    # Return the result
    result = total_legs
    return result

print(solution())