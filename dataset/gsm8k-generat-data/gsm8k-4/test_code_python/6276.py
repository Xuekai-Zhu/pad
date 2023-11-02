def solution():
    """Daliah picked up 17.5 pounds of garbage. Dewei picked up 2 pounds less than Daliah. Zane picked up 4 times as many pounds of garbage as Dewei. How many pounds of garbage did Zane pick up?"""
    # Define the weight of garbage picked up by Daliah
    daliah_garbage = 17.5

    # Define the weight of garbage picked up by Dewei
    dewei_garbage = daliah_garbage - 2

    # Define the weight of garbage picked up by Zane
    zane_garbage = dewei_garbage * 4

    # Return the weight of garbage picked up by Zane
    result = zane_garbage
    return result

print(solution())