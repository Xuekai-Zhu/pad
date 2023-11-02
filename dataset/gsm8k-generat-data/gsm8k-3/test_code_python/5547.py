def solution():
    """Frank has an apple tree in his backyard. 5 apples are hanging on the tree and 8 have fallen to the ground. If Frank's dog eats 3 of the apples off of the ground, how many apples are left?"""
    # Define the initial number of apples
    initial_apples = 5 + 8

    # Define the number of apples eaten by the dog
    dog_eaten = 3

    # Calculate the remaining number of apples
    remaining_apples = initial_apples - dog_eaten

    # Display the remaining number of apples
    result = remaining_apples
    return result

print(solution())