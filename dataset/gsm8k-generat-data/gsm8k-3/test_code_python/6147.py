def solution():
    """There are 6 dogs and 2 ducks in the garden. How many feet are there in the garden?"""
    # Define the number of feet for each animal
    DOG_FEET = 4
    DUCK_FEET = 2

    # Define the number of dogs and ducks in the garden
    num_dogs = 6
    num_ducks = 2

    # Calculate the total number of feet in the garden
    total_feet = (num_dogs * DOG_FEET) + (num_ducks * DUCK_FEET)

    # Display the total number of feet
    result = total_feet
    return result

print(solution())