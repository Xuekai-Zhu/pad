def solution():
    """A bushel of corn weighs 56 pounds and each individual ear of corn weighs .5 pounds. If Clyde picked 2 bushels of corn over the weekend, how many individual corn cobs did he pick?"""
    # Define the weight of one individual corn cob
    CORN_WEIGHT = 0.5

    # Define the weight of one bushel of corn
    BUSHEL_WEIGHT = 56

    # Define the number of bushels Clyde picked
    bushels_picked = 2

    # Calculate the total weight of the corn picked
    total_weight = BUSHEL_WEIGHT * bushels_picked

    # Calculate the number of individual corn cobs picked
    num_cobs = total_weight / CORN_WEIGHT

    # Display the number of cobs picked
    result = num_cobs
    return result

print(solution())