def solution():
    """Daliah picked up 17.5 pounds of garbage. Dewei picked up 2 pounds less than Daliah. Zane picked up 4 times as many pounds of garbage as Dewei. How many pounds of garbage did Zane pick up?"""
    # Define the weight of garbage Daliah picked up
    daliah_weight = 17.5

    # Define the weight of garbage Dewei picked up
    dewei_weight = daliah_weight - 2

    # Define the weight of garbage Zane picked up
    zane_weight = dewei_weight * 4

    # Display the weight of garbage Zane picked up
    result = zane_weight
    return result

print(solution())