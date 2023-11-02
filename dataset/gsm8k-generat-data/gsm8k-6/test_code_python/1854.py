def solution():
    # Calculate the total weight of corn picked by Clyde
    total_weight = 56 * 2  # 2 bushels of corn each weighing 56 pounds

    # Calculate the total number of individual corn cobs picked by Clyde
    total_cobs = total_weight / 0.5  # each individual corn cob weighs 0.5 pounds

    result = total_cobs
    return result

print(solution())