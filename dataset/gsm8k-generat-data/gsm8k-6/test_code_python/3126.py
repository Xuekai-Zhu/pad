def solution():
    # Calculate the total number of ears of corn to be planted
    total_ears = 70 * 4  # 4 kids planting rows of corn, each row has 70 ears

    # Calculate the total number of seeds needed for all the ears of corn
    total_seeds = 2 * total_ears  # 2 seeds per ear of corn

    # Calculate the number of bags of corn seeds needed
    bags_seeds = total_seeds / 48  # 48 seeds per bag

    result = bags_seeds / 4  # divide by 4 kids
    return result

print(solution())