def solution():
    """Chuck breeds dogs. He has 3 pregnant dogs. They each give birth to 4 puppies. Each puppy needs 2 shots and each shot costs $5. How much did the shots cost?"""
    # Define the number of pregnant dogs and puppies
    NUM_PREGNANT_DOGS = 3
    PUPPIES_PER_DOG = 4
    NUM_PUPPIES = NUM_PREGNANT_DOGS * PUPPIES_PER_DOG

    # Define the number of shots required for each puppy
    SHOTS_PER_PUPPY = 2

    # Define the cost per shot
    SHOT_COST = 5

    # Calculate the total cost of shots for all the puppies
    total_cost = NUM_PUPPIES * SHOTS_PER_PUPPY * SHOT_COST

    result = total_cost
    return result

print(solution())