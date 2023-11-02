def solution():
    """A bushel of corn weighs 56 pounds and each individual ear of corn weighs .5 pounds. If Clyde picked 2 bushels of corn over the weekend, how many individual corn cobs did he pick?"""
    # Define the weight of a bushel and the weight of an individual ear of corn
    BUSH_WEIGHT = 56
    EAR_WEIGHT = 0.5

    # Calculate the total weight of corn picked by Clyde
    total_weight = BUSH_WEIGHT * 2

    # Calculate the number of individual corn cobs picked by Clyde
    num_cobs = total_weight / EAR_WEIGHT

    result = int(num_cobs)
    return result

print(solution())