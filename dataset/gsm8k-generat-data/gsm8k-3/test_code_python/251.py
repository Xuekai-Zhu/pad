def solution():
    """Caleb picked a handful of dandelion puffs. He gave 3 to his mom, another 3 to his sister, 5 to his grandmother, and 2 to his dog. Then, he divided the remaining dandelion puffs equally among his 3 friends. How many dandelion puffs did each friend receive if he originally picked 40 dandelion puffs?"""
    # Define the number of dandelion puffs Caleb picked
    PICKED_PUFFS = 40

    # Calculate the number of dandelion puffs Caleb gave away
    GIVEN_PUFFS = 3 + 3 + 5 + 2

    # Calculate the number of dandelion puffs Caleb had left
    REMAINING_PUFFS = PICKED_PUFFS - GIVEN_PUFFS

    # Calculate the number of dandelion puffs each friend received
    FRIENDS_RECEIVED = REMAINING_PUFFS // 3

    # Display the number of dandelion puffs each friend received
    result = FRIENDS_RECEIVED
    return result

print(solution())