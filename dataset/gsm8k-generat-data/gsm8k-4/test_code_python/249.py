def solution():
    """Caleb picked a handful of dandelion puffs. He gave 3 to his mom, another 3 to his sister, 5 to his grandmother, and 2 to his dog. Then, he divided the remaining dandelion puffs equally among his 3 friends. How many dandelion puffs did each friend receive if he originally picked 40 dandelion puffs?"""
    # Define the initial number of dandelion puffs
    initial_puffs = 40

    # Calculate the number of puffs given away
    given_puffs = 3 + 3 + 5 + 2

    # Calculate the number of puffs remaining
    remaining_puffs = initial_puffs - given_puffs

    # Calculate the number of puffs each friend received
    friend_puffs = remaining_puffs / 3

    # Return the result
    result = friend_puffs
    return result

print(solution())