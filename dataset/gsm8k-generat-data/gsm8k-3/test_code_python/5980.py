def solution():
    """Chuck breeds dogs.  He has 3 pregnant dogs.  They each give birth to 4 puppies. Each puppy needs 2 shots and each shot costs $5.  How much did the shots cost?"""
    # Define the number of pregnant dogs and the number of puppies they have
    PREGNANT_DOGS = 3
    PUPPIES_PER_DOG = 4

    # Calculate the total number of puppies
    total_puppies = PREGNANT_DOGS * PUPPIES_PER_DOG

    # Calculate the total number of shots needed
    total_shots = total_puppies * 2

    # Calculate the total cost of the shots
    total_cost = total_shots * 5

    # Display the total cost of the shots
    result = total_cost
    return result

print(solution())