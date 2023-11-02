def solution():
    """Frank has an apple tree in his backyard. 5 apples are hanging on the tree and 8 have fallen to the ground. If Frank's dog eats 3 of the apples off of the ground, how many apples are left?"""
    # Define the initial number of apples
    initial_apples = 5

    # Define the number of apples that fell to the ground
    fallen_apples = 8

    # Define the number of apples that Frank's dog ate
    dog_eaten_apples = 3

    # Calculate the total number of apples left
    total_apples = initial_apples + fallen_apples - dog_eaten_apples

    # return the result
    result = total_apples
    return result

print(solution())